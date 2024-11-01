# Directed Acyclic Graph-Based Reasoning Framework for LLMs

This project is a Directed Acyclic Graph (DAG)-based reasoning framework designed to enhance the reasoning capabilities of Large Language Models (LLMs) such as GPT-2. The framework organizes and structures the reasoning process using DAGs, allowing for a logical flow of propositions, critiques, and refinements. This structured reasoning process can be visualized to provide insights into how the model iteratively improves its responses.

## **Features**
- **Propose, Critique, and Refine Reasoning**: The system allows users to initiate a reasoning cycle where an LLM provides an initial proposition, critiques it, and then refines the idea.
- **DAG Representation**: A Directed Acyclic Graph is used to represent the logical flow of reasoning.
- **Interactive Prompt**: Users can enter their own prompts to start a reasoning process and visualize the output.

## **Setup Instructions**

### **Prerequisites**
- Python 3.7 or higher
- Install dependencies listed in `requirements.txt` using `pip`


3. Ensure you have the appropriate data files in the data directory if you want to use preloaded examples.

## **Usage**
To start using the DAG-Based Reasoning Framework, you can run the `interactive_reasoning_app.py` script:

```sh
python interactive_reasoning_app.py
```

This script will prompt you for an input question, generate a proposition using GPT-2, critique the proposition, refine it, and visualize the process as a DAG.

### **Example Usage**

- **Prompt Provided by User**:
  ```
  Please enter a prompt to begin the reasoning process: What are the consequences of climate change on Arctic wildlife?
  ```

- **Output**:
  ```
  Proposition:
  Climate change is drastically affecting Arctic wildlife, particularly by reducing sea ice, which is a crucial habitat for animals like polar bears and seals.

  Critique:
  The statement does not account for other impacts such as changes in prey availability and increased human interference, which are also significant factors affecting Arctic wildlife.

  Refined Output:
  Climate change is affecting Arctic wildlife not only by reducing sea ice, which is crucial for polar bears and seals, but also by altering prey availability and increasing human interference, which adds additional pressures on these ecosystems.
  ```

- **DAG Visualization**:
  The Directed Acyclic Graph (DAG) representing the reasoning flow will be displayed using `matplotlib` and `networkx`. The graph will show nodes for each of the reasoning stages:
  - **Proposition**
  - **Critique**
  - **Refinement**


## **Code Structure**

- **`models/model_loader.py`**: Loads the pretrained model (default: GPT-2) and tokenizer.
- **`data/token_handler.py`**: Manages and adds special role-specific tokens (e.g., `<proposer>`, `<critic>`).
- **`reasoning/reasoning_cycle.py`**: Manages the core reasoning cycle, including generating, critiquing, and refining content.
- **`reasoning/dag_constructor.py`**: Constructs a DAG to represent the reasoning process.
- **`reasoning/topos_checker.py`**: Checks for logical consistency in the DAG.
- **`visualization/dag_visualizer.py`**: Visualizes the DAG representing the logical flow of reasoning.

## **Dependencies**
The project uses the following key Python libraries:
- **Transformers**: Hugging Face library to work with language models such as GPT-2.
- **NetworkX**: For graph creation and management.
- **Matplotlib**: To visualize the reasoning graph.

Ensure that all dependencies are installed by running:
```sh
pip install -r requirements.txt
```

## **Customization**
- You can change the language model used by modifying the `model_name` parameter in `ModelLoader`. 

## **Future Improvements**
- **Expand Model Compatibility**: Extend the project to use more sophisticated models such as GPT-3 or custom fine-tuned models.
- **Advanced DAG Analysis**: Add more complex validation and analysis features in `ToposChecker` to ensure logical consistency across more elaborate reasoning structures.
- **Web-Based Interface**: Develop a web-based user interface to make the interaction more user-friendly.

