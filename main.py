import gradio as gr
import pandas as pd
from helper_functions import load_dictionary, find_close_matches, calculate_distance

def tab1_function(word1, word2, metric):
    """
    Calculate edit distance between two words and find closest matches to word1.
    
    Parameters:
    word1, word2: str
        Words to compare.
    metric: str
        The distance metric to use.
        
    Returns:
    str, pd.DataFrame
        Distance between words and dataframe of closest matches.
    """
    if not word1 or not word2:
        return "Please enter both words.", None
    
    distance = calculate_distance(word1, word2, metric)
    dictionary = load_dictionary()
    matches = find_close_matches(word1, dictionary, metric)
    
    # dataframe for display
    df = pd.DataFrame(matches, columns=['Word', 'Distance'])
    
    return f"Distance between '{word1}' and '{word2}' using {metric}: {distance:.4f}", df

def tab2_function(word, metric):
    """
    Find closest matches for a given word.
    
    Parameters:
    word: str
        Word to find matches for.
    metric: str
        The distance metric to use.
        
    Returns:
    pd.DataFrame
        Dataframe of closest matches.
    """
    if not word:
        return None
    
    dictionary = load_dictionary()
    matches = find_close_matches(word, dictionary, metric)
    
    df = pd.DataFrame(matches, columns=['Word', 'Distance'])
    
    return df

def main():

    dictionary = load_dictionary()
    metrics = ["levenshtein", "damerau-levenshtein", "jaro", "jaro-winkler"]
    
    # Gradio interface
    with gr.Blocks(title="String Similarity Metrics", theme="soft") as app:
        gr.Markdown("# String Similarity Metrics")
        gr.Markdown("Calculate edit distances between words and find closest matches from the dictionary.")
        
        with gr.Tabs():
            with gr.Tab("Calculate Edit Distance"):
                with gr.Row():
                    with gr.Column():
                        word1_input = gr.Textbox(label="Word 1", placeholder="Enter first word")
                        word2_input = gr.Textbox(label="Word 2", placeholder="Enter second word")
                        metric_dropdown = gr.Dropdown(
                            choices=metrics, 
                            value="levenshtein", 
                            label="Select Distance Metric"
                        )
                        calculate_btn = gr.Button("Calculate")
                
                with gr.Row():
                    distance_output = gr.Textbox(label="Distance Result")
                
                with gr.Row():
                    gr.Markdown("### 10 Closest Words to Word 1")
                    matches_output = gr.DataFrame(label="Closest Matches")
                
                calculate_btn.click(
                    fn=tab1_function,
                    inputs=[word1_input, word2_input, metric_dropdown],
                    outputs=[distance_output, matches_output]
                )
            
            with gr.Tab("Find Closest Matches"):
                with gr.Row():
                    with gr.Column():
                        word_input = gr.Textbox(label="Search Word", placeholder="Enter a word to find matches")
                        metric_dropdown2 = gr.Dropdown(
                            choices=metrics, 
                            value="levenshtein", 
                            label="Select Distance Metric"
                        )
                        search_btn = gr.Button("Find Matches")
                
                with gr.Row():
                    closest_matches_output = gr.DataFrame(label="10 Closest Matches")
                
                search_btn.click(
                    fn=tab2_function,
                    inputs=[word_input, metric_dropdown2],
                    outputs=[closest_matches_output]
                )
    
    app.launch()

if __name__ == "__main__":
    main()