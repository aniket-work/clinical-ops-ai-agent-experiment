
import base64
import requests
import os

# Ensure images directory exists
os.makedirs("images", exist_ok=True)

diagrams = {
    "title_diagram": """
graph TD
    style ClinicalOps_AI_Agent fill:#f9f9f9,stroke:#333,stroke-width:2px
    
    subgraph ClinicalOps_AI_Agent [ClinicalOps AI Agent]
        direction TB
        
        A[Clinical Trial Data CSV] -->|Ingest| B(Data Processing)
        C[User Query] -->|NLP| D{Intent Recognition}
        
        B --> E[Visualization Module]
        D -->|Intent| E
        
        E -->|Generate| F[Matplotlib Charts]
        F -->|Report| G[Safety Insights]
    end
    """,
    
    "architecture": """
flowchart LR
    subgraph Data_Layer [Data Layer]
        CSV[(Clinical Data CSV)]
    end
    
    subgraph Intelligence_Layer [Intelligence Layer]
        Agent[ClinicalOps Agent]
        Parser[Query Parser]
        Plotter[Code Generator]
    end
    
    subgraph Presentation_Layer [Presentation Layer]
        CLI[Command Line Interface]
        Charts[PNG Visualizations]
    end
    
    CSV --> Agent
    Agent --> Parser
    Parser --> Plotter
    Plotter --> Charts
    CLI --> Agent
    
    style Data_Layer fill:#f5f5f5,stroke:#333,stroke-dasharray: 5 5
    style Intelligence_Layer fill:#e3f2fd,stroke:#1565c0
    style Presentation_Layer fill:#fff3e0,stroke:#e65100
    """
}

def generate_mermaid_images():
    print("🎨 Generating Mermaid Diagrams...")
    for name, code in diagrams.items():
        try:
            # Encoding the Mermaid code
            encoded_string = base64.b64encode(code.encode("utf-8")).decode("utf-8")
            url = f"https://mermaid.ink/img/{encoded_string}"
            
            print(f"   Downloading {name}...")
            response = requests.get(url)
            
            if response.status_code == 200:
                output_path = f"images/{name}.png"
                with open(output_path, 'wb') as f:
                    f.write(response.content)
                print(f"   ✅ Saved to {output_path}")
            else:
                print(f"   ❌ Failed to download {name}. Status: {response.status_code}")
        except Exception as e:
            print(f"   ❌ Error generating {name}: {e}")

if __name__ == "__main__":
    generate_mermaid_images()
