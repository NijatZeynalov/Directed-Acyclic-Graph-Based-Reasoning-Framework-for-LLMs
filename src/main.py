import matplotlib.pyplot as plt
import networkx as nx
from models.model_loader import ModelLoader
from data.token_handler import TokenHandler
from reasoning.reasoning_cycle import ReasoningCycle
from reasoning.dag_constructor import DAGConstructor
from visualization.dag_visualizer import DAGVisualizer

def main():
    model_loader = ModelLoader(model_name="gpt2")  #gpt model worked best
    token_handler = TokenHandler(tokenizer=model_loader.tokenizer)
    reasoning_cycle = ReasoningCycle(model_loader, token_handler)

    input_text = input("Please enter a prompt to begin the reasoning process: ")

    reasoning_cycle.initiate_reasoning()
    proposition = reasoning_cycle.propose(input_text)
    print("\nProposition:\n", proposition)

    critique = reasoning_cycle.critique(proposition)
    print("\nCritique:\n", critique)

    refined_output = reasoning_cycle.refine(proposition, critique)
    print("\nRefined Output:\n", refined_output)

    dag_constructor = DAGConstructor()
    dag_constructor.add_node("1", "proposition", proposition)
    dag_constructor.add_node("2", "critique", critique)
    dag_constructor.add_node("3", "refinement", refined_output)

    dag_constructor.add_edge("1", "2")  # Edge from proposition to critique
    dag_constructor.add_edge("2", "3")  # Edge from critique to refinement

    # Step 5: Visualize the DAG
    DAGVisualizer.draw_dag(dag_constructor.graph)

if __name__ == "__main__":
    main()
