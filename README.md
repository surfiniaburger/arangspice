# ArangSpice Project: A Spicy Blend of ArangoDB, LangChain, and NetworkX! 🌶️📊🕸️ (with Extra Flavor! 🍜)

## Inspiration 💡

This project was inspired by the hackathon's challenge of making complex health data both accessible and insightful – like turning a mountain of raw ingredients into a delicious, easy-to-digest meal! 🍲 We aimed to build a system capable of storing, retrieving, *and* meaningfully analyzing health data, going beyond simple queries to unlock deeper insights. We combined the power of graph databases (ArangoDB), natural language processing (LangChain), and advanced graph algorithms (NetworkX and more!) to create a truly versatile tool, directly addressing the hackathon's focus on **hybrid query capabilities**.

Our vision? A system to assist healthcare professionals, researchers, and public health officials. Imagine effortlessly identifying key individuals, understanding disease patterns within Massachusetts communities, exploring demographic influences on health outcomes, and tracking trends over time—all through simple, natural language interactions. It's like having a super-smart research assistant at your fingertips! 👩‍⚕️👨‍🔬

# Seamless GPU Acceleration with cuGraph and NetworkX

## Key Integration Point: `%env NX_CUGRAPH_AUTOCONFIG=True`

One of the most powerful aspects of our ArangSpice implementation is the seamless integration of NVIDIA's cuGraph for GPU-accelerated graph analytics. This integration is achieved through a single, crucial configuration:

```python
%env NX_CUGRAPH_AUTOCONFIG=True
import networkx as nx
```

### How It Works

This configuration enables transparent GPU acceleration without requiring any changes to our NetworkX code. Here's what happens behind the scenes:

1. Setting `NX_CUGRAPH_AUTOCONFIG=True` as an environment variable activates the cuGraph backend for NetworkX.

2. When we import NetworkX and call graph algorithms like:
   ```python
   centrality = nx.betweenness_centrality(G)
   communities = nx.community.louvain_communities(G)
   paths = nx.shortest_path(G, source=start_node)
   ```
   These operations are **automatically dispatched to cuGraph** and executed on the GPU when possible.

3. The results are returned in the expected NetworkX format, maintaining full compatibility with the rest of our codebase.

### Benefits of This Approach

- **Zero Code Changes**: We don't need to modify any algorithm calls or learn a new API - our existing NetworkX code runs with GPU acceleration.
  
- **Automatic Fallback**: If an algorithm isn't implemented in cuGraph or if no GPU is available, the system automatically falls back to standard NetworkX.
  
- **Massive Performance Gains**: For large-scale healthcare networks, this provides orders of magnitude speedup for computationally intensive operations like centrality calculations and community detection.

- **Hybrid Query Support**: This integration is essential for our hybrid query approach, allowing us to seamlessly combine AQL database operations with GPU-accelerated analytics.

### Real-World Impact

In ArangSpice, this transparent acceleration is particularly valuable for operations like:

- Identifying influential patients in large community networks
- Detecting clusters of related health conditions
- Calculating the shortest paths of disease transmission
- Performing community detection across patient populations

By leveraging this integration, ArangSpice delivers responsive performance even when analyzing complex relationships across thousands of patients and conditions in the Massachusetts healthcare dataset.

## What it does ⚙️

ArangSpice processes natural language queries about health data (focused on Massachusetts cities) stored within an ArangoDB graph database. It returns informative answers, *including* visualizations and AI-generated summaries. Think of it as a multi-course meal of data analysis:

*   **ArangoDB:** 🦊 The foundation – efficiently stores and retrieves complex, interconnected health data (patients, conditions, observations, demographics, etc., primarily within Massachusetts). It's the well-stocked pantry of our system.
*   **LangChain:** 🦜 The intelligent chef! It translates natural language requests into database queries (AQL), instructions for graph analysis, and human-readable summaries. It leverages the power of an **experimental version of Gemini (2.0 experimental 02-05)** as its LLM to understand user intent, generate AQL, and create insightful summaries.
*   **NetworkX:** 🕸️ Analyzes relationships *between* patients, conditions, and other entities. This is crucial for uncovering hidden connections, like finding influential individuals, common co-occurring conditions, and network-based patterns.
*   **Pandas & Seaborn:** 🐼📊 The statistical sous-chefs! They provide in-depth statistical analysis and visualization, particularly for exploring how demographic factors relate to healthcare metrics within Massachusetts communities.
*   **Gradio:** ⚡️ The friendly waiter! It provides a user-friendly, interactive web interface – no need to speak "database" or "code"!
*    **Gemini Multimodal Capabilities**: 🖼️📝 After generating initial visualizations and analyses, ArangSpice can leverage Gemini's multimodal capabilities. This means we could potentially:
    * **Create Abstract Visual Summaries**: Feed the generated charts and network graphs to Gemini and ask it to create a simplified, *abstract* visual representation that highlights a key finding. This could be a symbolic image, a stylized diagram, or even a visual metaphor that makes the insight easier to grasp at a glance.
    *   **Combine Visual and Textual Explanations:** Generate text summaries that directly reference and explain the abstract visualizations, providing a richer and more intuitive understanding of the data.

**Hybrid Query Power! ஹைபிரிட் வினவல் சக்தி!** (That's Tamil for "Hybrid Query Power!")

ArangSpice isn't *just* about individual tools; it's about how they work *together*, directly addressing the hackathon's core theme.  The magic of **hybrid queries** lies in the intelligent combination of:

*   **AQL + NetworkX/Pandas:** Many real-world health questions require a combination of direct database lookups (AQL) *and* more complex graph or statistical analysis. ArangSpice seamlessly blends these approaches, enabling powerful insights.  This is *exactly* what the hackathon called for!

* **Smart Routing (query_graph_with_smart_router):** This function is the brains of the operation. It uses pattern recognition to determine the *best* tool (or combination of tools) to answer a user's query, routing it to the appropriate specialized analysis function.

## Hackathon-Ready Hybrid Tools 🛠️ + Potential Use Cases 🏥

We built several tools specifically designed to leverage hybrid queries, perfectly aligning with the hackathon's requirements. Here are a few key examples, along with their potential use cases:

1.  **`healthcare_demographics_analysis`:**
    *   **Hybrid Power:** Combines AQL (to retrieve data based on location, demographic filters, and health conditions) with Pandas/Seaborn (for statistical analysis and visualization of demographic relationships).
    *   **Potential Use Cases:**
        *   **Health Equity Studies:** Identify disparities in healthcare access and outcomes across different demographic groups (e.g., income, ethnicity, age) within specific Massachusetts cities. This could inform targeted interventions to improve equity.
        *   **Resource Allocation:** Determine how healthcare resources should be allocated based on the demographic makeup and health needs of different communities.
        *   **Public Health Planning:** Understand how demographic factors influence the prevalence of specific conditions, allowing for more effective public health campaigns.

2.  **`healthcare_temporal_analysis`:**
    *   **Hybrid Power:** This tool is a prime example of a sophisticated hybrid approach. It uses:
        *   AQL to fetch time-based data (encounters, conditions, medications over a specified period).
        *   Pandas/Matplotlib to analyze and visualize trends, seasonality, and other temporal patterns (e.g., monthly counts, day-of-week distributions).
        *   **NetworkX** to create a network visualization of healthcare *events* (not just patients), showing how different events (encounters, conditions, medications) are related over time. This allows for the exploration of event sequences and relationships.
    *   **Potential Use Cases:**
        *   **Disease Outbreak Monitoring:** Track the spread of infectious diseases over time within Massachusetts, identifying potential outbreaks early on and visualizing the connections between different types of events.
        *   **Hospital Resource Management:** Predict fluctuations in patient volume based on historical trends and event relationships, allowing for optimized staffing and resource allocation.
        *   **Medication Usage Analysis:** Study how medication prescriptions change over time and how they relate to other healthcare events.
        *   **Seasonal Pattern Identification:** Determine if certain conditions or healthcare events have seasonal peaks, and visualize the temporal relationships between them.
        *   **Care Pathway Analysis:** Visualize and analyze common sequences of healthcare events (e.g., encounter -> condition -> medication), identifying potential bottlenecks or areas for improvement in patient care.  The NetworkX component is key here.

        *  **Identifying Root cause of readmission**: Identifying root cause of readmission using the timeline graph.
3.  **`text_to_patient_centrality`:**
    *   **Hybrid Power:** Employs AQL to filter patients based on specific criteria (e.g., location, conditions) and NetworkX to analyze the *connections* between those patients (based on shared conditions), calculating centrality scores to identify influential individuals.
    *   **Potential Use Cases:**
        *   **Identifying "Super-Spreaders":**  In the context of infectious diseases, identify patients who are highly connected within the network, potentially representing key individuals for targeted interventions (e.g., vaccination, education).
        *   **Key Opinion Leader (KOL) Identification:** Find influential patients who could serve as valuable resources for health education and outreach programs within their communities.
        *   **Understanding Disease Transmission:** Analyze the network structure to gain insights into how diseases spread within a population.

4.  **`medication_condition_cooccurrence_analysis`:**
    *   **Hybrid Power:**  This tool combines AQL and NetworkX to analyze the relationships between conditions, specifically focusing on those that co-occur with medication review conditions.
        *   **AQL:**  Used to identify patients who have undergone medication reviews and to retrieve all conditions associated with those patients.  This efficiently filters the initial dataset.
        *   **NetworkX:**  Used to build a network graph where *nodes* represent conditions and *edges* represent co-occurrences (two conditions appearing in the same patient).  This allows us to visualize and analyze the complex relationships between conditions.  Centrality measures (degree, betweenness, eigenvector) are calculated on this network to identify the most important/influential conditions.
    * **Potential Use Cases**:
        *   **Identifying Potential Adverse Drug Reactions:** By understanding which conditions frequently co-occur with medication reviews, healthcare professionals can be more alert to potential adverse drug reactions or interactions.
        *   **Improving Medication Management:**  The analysis can highlight conditions that might be contributing to the need for medication review, leading to better management of those underlying conditions.
        * **Refining Clinical Guidelines**: Provides insights that might help refine clinical practices and guidelines by showing common condition combinations for certain medications

5. **`calculate_condition_centrality`**:
        *   **Hybrid Power:** This tool leverages AQL and NetworkX to identify the most "central" or influential conditions with the patient condition networks..
            * **AQL or Networkx**: Used for querying conditions with patients.
            * **Networkx**: Used for creating graph and calculating centrality.
        *   **Potential Use Cases:**
            *   **Disease Prioritization:** Helps prioritize which conditions to focus on for public health interventions, based on their centrality in the network.
            *   **Research Focus:** Guides researchers towards conditions that may play a key role in disease pathways or comorbidities.
            *   **Understanding Disease Spread:**  In the context of infectious diseases, central conditions might be those that are more likely to be transmitted or to co-occur with other infections.


6. **`patient_location_analysis_tool`:**
    *   **Hybrid Power:** This tool powerfully combines AQL, NetworkX, Pandas, and Seaborn (through its internal use of `run_comprehensive_patient_analysis`).  It's designed for in-depth analysis of patient populations within specific locations in Massachusetts.
    * **What it does:**
        *   **Location-Based Filtering (AQL):**  Takes a natural language location query (e.g., "Boston", "Randolph Massachusetts") and uses AQL to efficiently retrieve patient data from ArangoDB, filtering by city and/or state.  It handles partial location names and attempts to infer the full location (e.g., adding "Massachusetts" to "Boston").
        *   **Network Graph Creation (NetworkX):**  Builds a NetworkX graph representing patients as nodes and connections between them based on shared characteristics (location, race, ethnicity, age group). This allows for the analysis of relationships *within* the specified location.
        *   **Centrality Analysis (NetworkX):**  Calculates various centrality metrics (degree, betweenness, closeness, eigenvector, and *custom* metrics like income centrality and risk score centrality) to identify influential or key patients within the network.
        *   **Statistical Analysis (Pandas/Seaborn):**  Calculates descriptive statistics and distributions for various patient attributes (age, gender, race, ethnicity, income, healthcare expenses). This provides a demographic and health profile of the patient population.
        * **Visualization (Matplotlib/Seaborn/Networkx):** Generates a comprehensive set of visualizations:
            *    Network graph visualizations (colored by different attributes like race, ethnicity, or community).
            *  Histograms and distributions of centrality metrics.
            *  Histograms and distributions of patient attributes (age, income, etc.).
            *   Community structure visualization (using the Louvain method).
        *   **AI-Powered Summary (Gemini):**  Generates a concise, human-readable summary of the analysis results, highlighting key findings and statistics.
        * **Return Complete Information:** Returns to the agent or user not just the summary but all raw information obtained in the process, such as :
            *  `"success": True/False`: Indicates success or failure and reason of failure if applicable.
            *  `"query"`: The original user query.
            *  `"full_query"`: The possibly inferred full query (with the state name filled up).
            *   `"summary"`: AI-generated summary.
            *   `"patient_count"`:  The number of patients found for the location.
            *   `"location_counts"`:  A breakdown of patient counts by location (city and state).
            *    `"key_stats"`:  A dictionary containing key statistics extracted from the analysis (e.g., gender distribution, age stats, top nodes by centrality).
            *    `"visualizations"`:  A dictionary of base64 encoded images (or file paths if saving to PNG is enabled) for the generated visualizations.
            *    `"raw_analysis"`:  The complete, raw analysis data, providing all the underlying calculations.
    *   **Potential Use Cases:**
        *   **Targeted Public Health Interventions:** Identify high-risk patients or communities within a specific location for targeted interventions (e.g., vaccination campaigns, health education programs).
        *   **Local Resource Allocation:**  Determine the specific healthcare needs of a community based on its demographics and health profile, informing resource allocation decisions.
        *   **Comparative Analysis:** Compare patient populations and health outcomes across different locations within Massachusetts.
        *   **Community Health Assessments:**  Provide a comprehensive overview of the health status and demographics of a particular community.

7. **`multi_stage_risk_analysis` (and supporting functions):**
    *    **Hybrid Power:** This is a *multi-stage* pipeline that exemplifies the core principles of the hackathon. It combines:
        *   **AQL:** For initial data retrieval and filtering (identifying the population of interest in a location).  A second AQL query enriches the data with related healthcare information (encounters, medications, conditions).
        *   **NetworkX:** To build a patient relationship graph (`build_patient_graph`) and calculate graph centrality metrics (degree, betweenness, closeness) within `calculate_patient_risk_scores`.  This allows us to incorporate network position into risk assessment.
        *   **Community Detection (Louvain algorithm):** To identify clusters of closely connected patients within the graph.
        *   **Custom Risk Scoring Logic:**  The `calculate_patient_risk_scores` function combines graph metrics (centrality) with patient-specific risk factors (provided as input) to generate a comprehensive risk score.
        *   **Data Integration and Reporting:**  The `integrate_analysis_results` function takes the outputs of all previous stages (AQL queries, graph analysis, community detection, risk scoring) and combines them into a comprehensive report, including:
            *   Summary statistics
            *   Lists of high, medium, and low-risk patients
            *   Community-level analysis (average risk, size, etc.)
            *   (Potentially, in a more complete implementation) Analysis of risk factor impact
            *   Detailed patient records
    *   **Potential Use Cases:** Proactive Patient Management, Targeted Interventions, Population Health Management, Resource Allocation, Clinical studies.
   * **Visualization Integration**:  Critically, this pipeline now includes a `visualize_risk_analysis_results` function. This function generates a suite of visualizations *directly* from the analysis results, including:
        *   **Risk Distribution Histogram:** Shows the distribution of patient risk scores.
        *   **Risk Category Pie Chart:** Displays the proportion of patients in each risk category (high, medium, low).
        *   **Network Visualization:**  A NetworkX-powered visualization of the patient network, colored by risk score and showing community structure.
        *   **Community Risk Boxplot:**  Compares the distribution of risk scores across different patient communities.
        *   **Demographics Analysis:**  Visualizes demographic breakdowns (age, gender, race, ethnicity) by risk level.
        *   **Medical Conditions Heatmap:**  Shows the prevalence of top medical conditions across different risk levels.
        *   **Geographic Visualization:**  (Currently a bar chart by state; could be expanded to a map).
        * **Interactive HTML Dashboard:** Combines all the visualizations into an interactive HTML dashboard for easy exploration.  This dashboard is saved to the file system.

These tools, and the underlying `query_graph_with_smart_router`, demonstrate a clear commitment to the hackathon's emphasis on hybrid query approaches.  They showcase the power of combining ArangoDB's graph capabilities with the analytical strengths of NetworkX and Pandas, all orchestrated by LangChain.

## How we built it 🏗️

1.  **Setup and Environment:** Installed ArangoDB, and all required Python libraries.
2.  **Data Loading:** Loaded the `SYNTHEA_P100` dataset (focused on Massachusetts) into ArangoDB.
3.  **LangChain Tools:** Defined core LangChain tools (`@tool` functions):
    *   `text_to_aql_to_text`: Basic AQL query execution.
    *   The hybrid tools listed above (`healthcare_demographics_analysis`, `healthcare_temporal_analysis`, `text_to_patient_centrality`).
    *   Supporting tools like `analyze_medication_review_conditions`, `text_to_condition_centrality`, `visualize_isolated_patients`, and `generate_network_visualization`.
4.  **Agent Creation:** Used `langgraph.prebuilt.create_react_agent` to create a LangChain ReAct agent, enabling intelligent tool selection.
5.  **Gradio Interface:** Created a user-friendly web interface with Gradio.
6.  **Risk Analysis Pipeline:** Implemented the `multi_stage_risk_analysis` pipeline, including supporting functions like `calculate_patient_risk_scores` and `integrate_analysis_results`, to demonstrate a complex, multi-step hybrid analysis workflow.

## Challenges we ran into 🚧

*   **Dependency Management:** Ensuring all libraries worked together.
*   **LLM Prompt Engineering:** Crafting prompts for accurate AQL queries and analysis.
*   **Data Complexity:** Handling the interconnected health data.
*   **Visualization Integration:** Integrating visualizations into the Gradio interface.
* **Error Handling**: Dealing with call of non-existing tool

## Accomplishments that we're proud of 🎉

*   **Working Prototype:** A functional system answering a wide range of questions.
*   **Multiple Hybrid Analysis Tools:** Seamless integration of AQL, NetworkX, and Pandas/Seaborn.
* **Comprehensive Risk Analysis Pipeline:** We've built a complete pipeline, from data retrieval to visualization, for assessing patient risk. This goes beyond simple queries and demonstrates a sophisticated, multi-stage analysis workflow.
* **Dynamic Visualizations:** The `visualize_risk_analysis_results` function creates a suite of insightful visualizations directly from the analysis output. This makes the results much easier to understand and interpret.
* **Interactive Dashboard:** The HTML dashboard provides a user-friendly way to explore the visualizations and gain a holistic understanding of the analysis.
*   **Interactive Visualizations:** Gradio interface with data visualizations.
*   **AI-Powered Summaries:** LLM-generated summaries of analysis results.
* **User-Friendly Interface**
* **Direct Hackathon Alignment:**  A strong focus on hybrid query approaches, as emphasized by the hackathon.

## What we learned 📚

*   **ArangoDB:** Deepened understanding of graph databases.
*   **LangChain:** Building custom tools and agents.
*   **Network Analysis (NetworkX):** Analyzing patient networks.
*   **Statistical Analysis (Pandas, Seaborn):** Exploring demographic relationships.
*   **Prompt Engineering:** Crafting effective LLM prompts.
*   **Gradio:** Building interactive web interfaces.
* **Hybrid Approaches:** The power of combining different analysis techniques.

## What's next for ArangSpice 🌶️➡️🔮

*   **Expanded Query Capabilities:** More sophisticated temporal analysis and comparisons.
*   **Additional Datasets:** Integrate other relevant datasets.
*   **Enhanced Visualizations:** More advanced and interactive visualizations.
*   **Improved Error Handling:** More robust error handling and user feedback.
*   **User Authentication:** Secure access.
*   **Scalability:** Optimization for larger datasets.
*   **Deployment:** Cloud deployment for wider accessibility.
*   **Fine-Tuning:** LLM fine-tuning on medical data.
* **UI Improvements:** Continuously improve the user interface.
* **Leveraging Gemini's Multimodal Strengths:** Implement the abstract visual summary generation using Gemini, as described in the "What it does" section. This would involve:
    *   Creating a new LangChain tool (or integrating it into existing tools) that takes the generated visualizations (from NetworkX, Matplotlib, Seaborn) as input.
    *   Crafting a prompt for Gemini that instructs it to create a simplified, abstract visual representation of a key finding.
    *   Processing the output from Gemini (which could be an image or a description of an image) and displaying it in the Gradio interface.

We believe ArangSpice has the potential to be a powerful tool for healthcare research and analysis, and we're excited to continue developing it! Stay tuned for more spicy updates! 🌶️🔥

[relevant packages](https://ai.google.dev/gemini-api/docs/downloads)