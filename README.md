```python
# 🚀 Arangspice.ipynb: Key Concepts & Code Highlights

# This notebook combines ArangoDB, LangChain, and NetworkX for health data analysis. Here's a breakdown of the key parts:

# ## 1. Installations 📦

# ```python
# # Core libraries (PyTorch, ArangoDB, NetworkX, LangChain, Gradio, RAPIDS cuGraph)
# !pip install ...
# ```

# Installs all necessary packages.  Crucially, this includes libraries for machine learning (PyTorch), graph databases (ArangoDB, `nx-arangodb`), graph analysis (NetworkX, `nx-cugraph`), LLM interaction (LangChain), and UI creation (Gradio).

# ## 2. LangChain Tools 🛠️

# Two key LangChain tools are defined:

# *   **`text_to_aql_to_text(query: str) -> str`**:  Converts natural language to AQL (ArangoDB Query Language), executes the query, and returns a natural language response.
#     ```python
#     @tool
#     def text_to_aql_to_text(query: str) -> str:
#         # ... (Uses LLM to generate AQL, then ArangoGraphQAChain to execute) ...
#     ```

# *   **`text_to_nx_algorithm_to_text(query: str) -> str`**: Converts natural language to NetworkX code for graph analysis, executes it, and returns a natural language response.
#     ```python
#     @tool
#     def text_to_nx_algorithm_to_text(query: str) -> str:
#       #Calls an undefined function
#       result = analyze_patient_network(db, query, model)
#     ```

# ## 3. ArangoDB Connection & Graph Setup ⚙️

# ```python
# db = ArangoClient(hosts="ARANGO_HOST").db(...)
# datasets = Datasets(db)
# datasets.load("SYNTHEA_P100")
# G_adb = nxadb.Graph(name="SYNTHEA_P100", db=db)
# ```

# Connects to your ArangoDB database, loads the `SYNTHEA_P100` dataset, and creates a NetworkX graph object (`G_adb`) representing the database.  This allows both AQL and NetworkX operations.

# ## 4. Agent Creation 🤖

# ```python
# from langgraph.prebuilt import create_react_agent

# tools = [text_to_aql_to_text, text_to_nx_algorithm_to_text]

# def query_graph(query):
#     llm = model
#     app = create_react_agent(llm, tools)
#     # ...
# ```

# Creates a LangChain agent (`create_react_agent`) that can use the defined tools and an LLM to process user queries.  The `query_graph` function provides a simple interface to interact with the agent.

# ## 5. Smart Query Router 🤔

# ```python
# def query_graph_with_smart_router(query):
#     # ... (Uses regular expressions to categorize the query) ...
#     if matched_category == 'location_distribution':
#         # ...
#     elif matched_category == 'influential_patients':
#        # ... text_to_nx_algorithm_to_text(query)
#     elif matched_category == 'condition_analysis':
#         # ... text_to_aql_to_text(query)
#     # ...
# ```

# This function attempts to intelligently route the query to the most appropriate tool (or a specific function) based on pattern matching.  It's a more sophisticated way to handle user input than just passing everything to the agent.

# ## 6. Database Check & Geographic Analysis 🌍

# ```python
# def comprehensive_db_check(db_connection):
#   #Checks fields using AQL

# def get_geographic_condition_data(db_connection, condition=None, limit=1000):
#     # ... (AQL query to get patient geographic data) ...

# def get_condition_by_state(db_connection, top_n_conditions=5):
#   #Retrieves and processes geographic information.

# def create_geographic_visualizations(db_connection):
#  #Creates visualizations

# def enhance_dashboard_with_geographic_data(db_connection, existing_dashboard_data=None):
#   #Combines data

# def display_enhanced_dashboard(dashboard_data):
#  #Displays dashboard

# def create_enhanced_gradio_interface(db_connection):
#  #Creates gradio interface
# ```

# These functions perform:

# *   **Database structure check** (`comprehensive_db_check`): Uses AQL to examine the available data fields.
# *   **Geographic data retrieval**:  `get_geographic_condition_data` and `get_condition_by_state` use AQL to fetch patient data with location and condition information.
# *   **Visualization**: `create_geographic_visualizations` uses `plotly` to create maps and charts.
# *   **Dashboard**:  `enhance_dashboard_with_geographic_data`, `display_enhanced_dashboard` and `create_enhanced_gradio_interface` combines and presents the data, including a Gradio interface.

# ## 7. Gradio Interface 📊

# ```python
# import gradio as gr

# gr.Interface(fn=query_graph_with_smart_router, inputs="text", outputs="text").launch(share=True)
# ```

# Finally, a simple Gradio interface is launched, allowing users to interact with the `query_graph_with_smart_router` function through a web UI.

```

Care coordination analysis leverages the structure of patient networks to identify key individuals and clusters, providing actionable insights for healthcare systems. Here’s how it benefits society:

Identifying Key Patient Hubs: By determining which patients are most connected—using metrics like degree or betweenness centrality—healthcare providers can focus on those individuals who may have more complex needs or who could potentially act as “bridges” between different patient groups. Targeted interventions for these key patients can reduce hospital readmissions, prevent complications, and lower overall healthcare costs.

Understanding Patient Communities: Community detection helps uncover clusters of patients who share similar risk factors, behaviors, or care pathways. By understanding these groups, care teams can design tailored care coordination programs (such as patient-centered medical homes or integrated care teams) that address specific needs, promote preventive care, and improve health outcomes.

Optimizing Resource Allocation: Analyzing the network structure reveals how resources—like specialty care, follow-up services, or social support—can be better distributed. For instance, knowing the largest patient community may allow providers to implement community-based interventions, ensuring that scarce resources reach those who are most interconnected and vulnerable.

Informing Public Health Policy: Insights from network analysis can guide public health strategies. By modeling care coordination through synthetic data, policymakers can simulate various interventions, predict outcomes, and implement strategies that not only improve individual patient care but also enhance the overall efficiency and equity of the healthcare system.

Overall, this approach empowers healthcare systems to move from a one-size-fits-all model to more personalized, data-driven care coordination. It ultimately leads to better patient outcomes, reduced costs, and a more resilient healthcare infrastructure that benefits society as a whole.




gcloud compute networks subnets update my-vpc-network \
    --region=us-east1 \
    --enable-private-ip-google-access



gcloud compute networks subnets describe my-vpc-network \
    --region=us-east1 \
    --format="get(privateIpGoogleAccess)"

gcloud compute networks subnets create starscraper-subnet-us-central1 \
    --network=starscraper-vpc \
    --region=us-central1 \
    --range=10.128.0.0/20 \
    --enable-private-ip-google-access


gcloud compute firewall-rules create allow-all-internal \
    --network=starscraper-vpc \
    --allow=tcp,udp,icmp \
    --source-ranges=10.128.0.0/20 

gcloud compute networks subnets create starscraper-subnet-europe-west1 \
    --network=starscraper-vpc \
    --region=europe-west1 \
    --range=192.168.0.0/16 \
    --enable-private-ip-google-access


gcloud compute networks subnets describe starscraper-subnet-europe-west1 \
    --region=europe-west1 \
    --format="get(privateIpGoogleAccess)"


gcloud compute networks subnets update starscraper-subnet-europe-west1 \
    --region=us-central1 \
    --enable-private-ip-google-access


The error message indicates that the organization policy constraints/compute.vmExternalIpAccess is preventing your instance from being assigned an external IP address. You need to modify this constraint to allow your instance to have an external IP.

First, create a JSON file named policy.json with the following content, replacing the placeholders with your project ID, zone, and instance name:

{
  "constraint": "constraints/compute.vmExternalIpAccess",
  "listPolicy": {
    "allowedValues": [
      "projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME"
    ]
  }
}
Generated code may be subject to license restrictions not shown here. Use code with care. Learn more 





Video Script: GraphRAG and the Future of Data Analysis

(0:00-0:15) Intro - Energetic and Engaging

(Visual: Fast-paced montage of historical data representations: abacus, punch cards, early computers, modern dashboards, graph visualizations, ending with your project's logo/title.)

(Narrator): "Data. It's the lifeblood of, well, everything these days. But how we use that data? That's been a wild ride. We're going to take a quick trip through time, from counting on our fingers to building the future of AI-powered insight... and show you how our project fits into that revolution!"

(0:15-1:30) A Brief History of Data Analysis

(Visual: Split screen. One side shows historical images, the other shows modern equivalents.)

Left: Ancient clay tablets, counting sticks. Right: Spreadsheets.

Left: Early mechanical calculators. Right: Early programming languages (FORTRAN, COBOL).

Left: Punch cards, magnetic tape. Right: Relational databases (SQL).

Left: Early computer terminals, static charts. Right: Business Intelligence (BI) dashboards.[1]

(Narrator): "For centuries, 'data analysis' meant basic counting and record-keeping. Think clay tablets and abacuses! [Source: A Brief History of Data Analysis - GeeksforGeeks [31]] The mid-20th century brought the first computers – ENIAC, anyone? [Source: A Brief History of Data Analysis - GeeksforGeeks [31]] – and suddenly, we could do way more, but it was still incredibly limited. We had early programming languages like FORTRAN and COBOL to help with statistical calculations.[2] [Source: A Brief History of Data Analysis - GeeksforGeeks [31]]"

(Narrator): "Then came the relational database revolution in the 70s and 80s. SQL became the king, and we could finally organize data in tables and ask structured questions. [Source: Graph database - Wikipedia [21]] But... the world isn't just tables. What about connections?"

(Narrator):"The late 20th and early 21st centuries brought us Business Intelligence (BI) tools.[1] [Source: The Evolution of Modern Data Analytics: From Spreadsheet to AI-Powered Insights - IABAC [30]] Suddenly, even non-technical users could create interactive dashboards. [Source: The Evolution of Modern Data Analytics: From Spreadsheet to AI-Powered Insights - IABAC [30]] But these were mostly about looking backwards – what happened?"

(1:30-2:30) The Rise of Big Data and the Need for Graphs

(Visual: Exploding data visualizations – social networks, interconnected devices, complex systems.)

(Narrator): "Then... the internet exploded. Social media, the Internet of Things, everything became connected. We entered the era of Big Data – volume, velocity, variety.[1] [Source: The Evolution of Modern Data Analytics: From Spreadsheet to AI-Powered Insights - IABAC [30]] Traditional databases started to struggle. Think about it: how do you represent a social network – with all its friendships, groups, and interactions – in a table? It gets messy, fast."

(Narrator): "That's where graph databases come in. They're designed to handle relationships as first-class citizens. [Source: Graph database - Wikipedia [21], What is a Graph Database? - Graph DB Explained - AWS [19]] Instead of rows and columns, you have nodes (things) and edges (connections). It's a much more natural way to represent many real-world scenarios."

(Narrator): "And the growth? It's explosive. The graph database market is projected to reach billions of dollars in the next few years, with a compound annual growth rate of around 25%![3] [Source: Graph Database Market Overview - Nebula Graph [39], Graph Database Market Size & Share, Industry Report 2032 - GMI Insights [43]] This isn't a niche technology anymore; it's becoming essential."

(2:30-3:30) Introducing GraphRAG and Agentic AI

(Visual: Shift to more abstract representations of AI, agents, and knowledge graphs.)

(Narrator): "But even with graph databases, we still faced challenges. How do we combine the power of graphs with the natural language understanding of large language models (LLMs)? That's where Retrieval-Augmented Generation (RAG) came in. RAG lets LLMs pull in relevant information to give better answers.[4][5] But traditional RAG often misses the connections."[4]

(Narrator): "Enter GraphRAG! It's the next evolution. Instead of just grabbing text snippets, GraphRAG uses a knowledge graph to understand the relationships between pieces of information.[4][6] [Source: GraphRAG vs. Baseline RAG: Solving Multi-Hop Reasoning in LLMs - GenUI [7], RAG vs GraphRAG - DEV Community [6]] This means more accurate, more complete, and more contextual answers."

(Narrator): "And we're taking it even further. We're building an agentic application. This isn't just about answering questions; it's about an AI agent that can reason, plan, and act on the graph data. [Source: What Is Agentic AI? - NVIDIA Blog [33], Transforming Data Analytics Through Agentic AI - Tellius [5]] Think of it as a super-smart analyst that can explore the data, find insights, and even make recommendations – all autonomously."

(3:30-4:30) Our Project: [Your Project Name]

(Visual: Screenshots and demos of your project. Focus on the user interface, the queries being asked, and the results being displayed. Highlight the graph visualizations.)

(Narrator): "So, what did we build? We created Arangspice, an agentic application that analyzes patient data using GraphRAG and the power of ArangoDB and NVIDIA cuGraph."

(Narrator): "We used the Synthea dataset, which represents a network of patients, conditions, and observations. Our agent can answer complex questions like, 'Find the top 5 most influential patients with diabetes in North Carolina.'"

(Demo - show the query being entered and the results. Highlight the AQL query and the NetworkX analysis): "You can see here, we're not just getting a list of names. Our agent uses AQL to find the relevant patients, then uses NetworkX – and, ideally, cuGraph for GPU acceleration – to calculate centrality measures. This tells us who is most connected within the network of patients with diabetes."

(Narrator): "We used a smart router, allowing for the query to go to the correct tool."

(Demo - show the LLM-generated summary): "Finally, the agent uses an LLM to explain why these patients are influential. It's not just data; it's insight."

(4:30-5:00) The Future and Call to Action

(Visual: Forward-looking visuals – interconnected networks, AI agents, data-driven decisions.)

(Narrator): "This is just the beginning. We believe that agentic applications, powered by GraphRAG, are the future of data analysis. Imagine this applied to:

Financial fraud detection: Finding hidden connections between suspicious transactions. [Source: Graph Database Use Case in Fraud Detection - PuppyGraph [15]]

Personalized medicine: Tailoring treatments based on a patient's unique network of health data. [Source: Discover 5 GraphRAG applications for your business - Lettria [27]]

Supply chain optimization: Identifying bottlenecks and improving efficiency. [Source: Discover 5 GraphRAG applications for your business - Lettria [27]]

Cybersecurity: Identifying and mitigating complex threats by analyzing network activity. [Source: What is a Graph Database and What are the Benefits of Graph Databases - Nebula Graph [26]]"

(Narrator): "We're excited to be part of this revolution, and we hope you are too! Thanks for watching, and check out our project on Devpost!"

Key improvements and explanations:

Clear Narrative: The script tells a story, starting with the history and progressing to the future.

Engaging Tone: It's less formal and more conversational, suitable for a hackathon audience.

Visual Emphasis: The script explicitly calls out visuals, which are crucial for a video.

Concise Explanations: Complex concepts like RAG, GraphRAG, and agentic AI are explained simply and clearly.

Project Focus: The script seamlessly integrates the project demonstration into the broader narrative.

Future-Oriented: It emphasizes the potential of the technology and the project.

Call to Action: It ends with a clear call to action (visit the Devpost page).

Sources: The video includes sources for statistics.

Statistics: The script now includes several relevant statistics to back up the claims about the growth and importance of graph databases and related technologies. The growth of graph databases is substantial.[3][7]

This improved script provides a strong foundation for your hackathon video. Remember to keep the visuals engaging and the explanations clear and concise. Good luck!








GraphRAG (Retrieval-Augmented Generation): The function implements a GraphRAG approach. It combines structured data retrieval from a graph database (ArangoDB) with the generative capabilities of a Large Language Model (LLM). This allows for a richer, more contextualized analysis than either technique could provide alone. The function retrieves data, performs graph calculations, and then augments the LLM's generation with this retrieved information.

Dynamic Subgraph Creation and Analysis: Instead of analyzing the entire patient graph (which could be very large), the function intelligently extracts a relevant subgraph based on the user's query. This subgraph focuses on patients in a specific location and, optionally, with a specific condition. This targeted approach improves efficiency and the relevance of the analysis.

Multi-faceted Centrality Analysis: The code calculates multiple centrality measures (degree, betweenness, and eigenvector centrality), and then combines them into a weighted composite score. This provides a more nuanced view of patient influence within the network than any single measure would. The weighting (0.5 for degree, 0.3 for betweenness, and 0.2 for eigenvector) prioritizes degree centrality, reflecting its importance in this context. The function also handles potential errors during centrality calculations, providing fallback mechanisms.



AQL Query:

The build_patient_query_with_expanded_location function constructs an AQL (ArangoDB Query Language) query based on the user's input (condition and location). This query efficiently retrieves relevant patient data from the database.

The query uses FILTER clauses to select patients matching the specified location (using the expanded location terms).

If a condition is specified, it filters for patients associated with that condition via the patients_to_conditions edge collection.

It also retrieves observations for each patient from the patients_to_observations edge collection, limiting observations to the past year.

The query uses traversals (1..1 OUTBOUND for conditions, 1..3 OUTBOUND for observations) to efficiently navigate the graph relationships.

Graph Construction (NetworkX/CuGraph):

The build_patient_graph function takes the results of the AQL query (a list of patient data) and constructs a NetworkX graph.

Each patient becomes a node with type='patient'.

Each unique condition becomes a node with type='condition'.

Each unique observation (combination of observation code and value) becomes a node with type='observation'.

Edges are created to represent relationships: has_condition edges between patients and conditions, and has_observation edges between patients and observations.

Centrality Calculations:

The calculate_multiple_centrality_measures function calculates three centrality measures:

Degree Centrality: The number of connections a node has. A patient connected to many conditions and observations will have a high degree centrality. The function tries nx.degree_centrality(G) first. If that fails (which can happen in some graph configurations), it falls back to a manual calculation: len(list(G.neighbors(node))) / max(1, len(G) - 1). This fallback calculates the degree and normalizes it by the maximum possible degree.

Betweenness Centrality: Measures how often a node lies on the shortest path between other nodes. A patient who connects disparate parts of the network (e.g., patients with different conditions) will have high betweenness. It attempts to use nx.betweenness_centrality(G, k=min(10, G.number_of_nodes())). The k parameter limits the number of nodes considered for performance reasons. If this fails, or if the graph has fewer than 3 nodes, it sets betweenness to 0.0 for all nodes.

Eigenvector Centrality: Measures a node's influence based on the influence of its neighbors. A patient connected to other highly influential patients will have high eigenvector centrality. It tries nx.eigenvector_centrality_numpy(G) (the NumPy version is often more stable). If this fails, or if the graph is not connected or has only one node, it sets eigenvector centrality to 0.0 for all nodes.

Normalization: Each centrality measure is normalized to a 0-1 range. This is crucial for combining them into a composite score. The normalization formula is: (value - min_val) / (max_val - min_val). It skips normalization if all values for a measure are 0.

Composite Centrality: The three normalized centrality measures are combined into a single composite score using a weighted average: weighted_sum = (0.5 * degree) + (0.3 * betweenness) + (0.2 * eigenvector).

