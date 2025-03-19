import base64
import os
from google import genai
from google.genai import types


def save_binary_file(file_name, data):
    f = open(file_name, "wb")
    f.write(data)
    f.close()


def generate():
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    files = [
        # Make the file available in local system working directory
        client.files.upload(file="centrality_my_metric.png"),
        # Make the file available in local system working directory
        client.files.upload(file="centrality_location.png"),
        # Make the file available in local system working directory
        client.files.upload(file="centrality_healthcare_cost.png"),
        # Make the file available in local system working directory
        client.files.upload(file="centrality_demographic.png"),
        # Make the file available in local system working directory
        client.files.upload(file="centrality_eigenvector.png"),
        # Make the file available in local system working directory
        client.files.upload(file="centrality_degree.png"),
        # Make the file available in local system working directory
        client.files.upload(file="centrality_closeness.png"),
        # Make the file available in local system working directory
        client.files.upload(file="centrality_betweenness.png"),
        # Make the file available in local system working directory
        client.files.upload(file="network_race.png"),
        # Make the file available in local system working directory
        client.files.upload(file="network_ethnicity.png"),
        # Make the file available in local system working directory
        client.files.upload(file="attribute_race.png"),
        # Make the file available in local system working directory
        client.files.upload(file="centrality_age.png"),
        # Make the file available in local system working directory
        client.files.upload(file="attribute_income.png"),
        # Make the file available in local system working directory
        client.files.upload(file="attribute_healthcare_expenses.png"),
        # Make the file available in local system working directory
        client.files.upload(file="network_gender.png"),
        # Make the file available in local system working directory
        client.files.upload(file="community_structure.png"),
        # Make the file available in local system working directory
        client.files.upload(file="attribute_gender.png"),
        # Make the file available in local system working directory
        client.files.upload(file="attribute_ethnicity.png"),
        # Make the file available in local system working directory
        client.files.upload(file="attribute_age.png"),
    ]
    model = "gemini-2.0-flash-exp-image-generation"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_uri(
                    file_uri=files[0].uri,
                    mime_type=files[0].mime_type,
                ),
                types.Part.from_uri(
                    file_uri=files[1].uri,
                    mime_type=files[1].mime_type,
                ),
                types.Part.from_uri(
                    file_uri=files[2].uri,
                    mime_type=files[2].mime_type,
                ),
                types.Part.from_uri(
                    file_uri=files[3].uri,
                    mime_type=files[3].mime_type,
                ),
                types.Part.from_uri(
                    file_uri=files[4].uri,
                    mime_type=files[4].mime_type,
                ),
                types.Part.from_uri(
                    file_uri=files[5].uri,
                    mime_type=files[5].mime_type,
                ),
                types.Part.from_uri(
                    file_uri=files[6].uri,
                    mime_type=files[6].mime_type,
                ),
                types.Part.from_uri(
                    file_uri=files[7].uri,
                    mime_type=files[7].mime_type,
                ),
                types.Part.from_uri(
                    file_uri=files[8].uri,
                    mime_type=files[8].mime_type,
                ),
                types.Part.from_uri(
                    file_uri=files[9].uri,
                    mime_type=files[9].mime_type,
                ),
                types.Part.from_uri(
                    file_uri=files[10].uri,
                    mime_type=files[10].mime_type,
                ),
                types.Part.from_uri(
                    file_uri=files[11].uri,
                    mime_type=files[11].mime_type,
                ),
                types.Part.from_uri(
                    file_uri=files[12].uri,
                    mime_type=files[12].mime_type,
                ),
                types.Part.from_uri(
                    file_uri=files[13].uri,
                    mime_type=files[13].mime_type,
                ),
                types.Part.from_uri(
                    file_uri=files[14].uri,
                    mime_type=files[14].mime_type,
                ),
                types.Part.from_uri(
                    file_uri=files[15].uri,
                    mime_type=files[15].mime_type,
                ),
                types.Part.from_uri(
                    file_uri=files[16].uri,
                    mime_type=files[16].mime_type,
                ),
                types.Part.from_uri(
                    file_uri=files[17].uri,
                    mime_type=files[17].mime_type,
                ),
                types.Part.from_uri(
                    file_uri=files[18].uri,
                    mime_type=files[18].mime_type,
                ),
                types.Part.from_text(text="""
> \"You are an AI assistant skilled at interpreting network analysis visualizations and identifying potential overarching findings within patient network data. You will analyze the attached set of images [**list the key visuals you have generated so far, e.g., 'Highlighted Patient Network with Betweenness Centrality and Gender Coloring', 'Comparative Centrality Bar Chart for Gender', 'Community Structure with Demographic Overlay'**].
>
> **Step 1: Identify Potential Overarching Findings:** Based on these visualizations, identify several potentially interesting overarching findings related to:
>
> *   **Centrality and Demographics:** Are certain demographic groups (e.g., gender, race, age range) consistently exhibiting higher or lower centrality across different metrics?
> *   **Centrality and Community Structure:** Are the most central individuals disproportionately located within specific communities? Do certain communities have higher average centrality scores?
> *   **Demographic Distribution within Communities:** Are certain communities primarily composed of specific demographic groups?
> *   **Relationships between Different Centrality Metrics and Demographics/Communities:** Are there correlations between how central someone is (by one measure) and their demographic characteristics or community affiliation?
> *   **Unusual Patterns or Outliers:** Are there any visually striking patterns or individual nodes that seem particularly influential or isolated?
>
> **Step 2: Suggest Findings to the User:** Based on your analysis in Step 1, generate a list of 2-3 of the most potentially interesting overarching findings in simple, non-technical language. Frame these as questions or statements that would pique the user's interest. For example:
>
> *   'It appears that female patients tend to be more central connectors within the network. Would you like a simplified visualization focusing on this?'
> *   'We've observed that a particular community seems to have a higher number of highly influential individuals. Shall we visualize this further?'
> *   'The data suggests a potential link between age group and how easily patients can reach others in the network. Would you be interested in seeing a simplified representation of this?'
>
> **Step 3: Await User Selection:** Present these suggested findings to the user and ask them to select one they would like to visualize in a simplified, abstract manner.
>
> **Step 4: Generate Simplified Visualization (Important):** Once the user selects a finding, proceed with the following instruction: 'Based on the user's selected overarching finding: [**user's selection**], generate a simplified, abstract visual representation that effectively communicates this core insight. This visualization should be easy to grasp at a glance and should not necessarily be a direct representation of the original network graph. Think in terms of symbolic representations, comparative shapes/sizes, or thematic colorings. Briefly explain the abstract visualization you create (1-2 sentences).'
>
> **Step 5: Offer to Explore Other Findings:** After generating the visualization in Step 4, prompt the user by saying: 'Would you like to explore a simplified visualization for any of the other potential findings I identified earlier?' If the user says yes, return to Step 2 with the remaining findings.\"
"""),
            ],
        ),
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text="""Here's an analysis of the provided visualizations to identify potential overarching findings:

**Step 1: Identify Potential Overarching Findings:**

*   **Centrality and Demographics:**
    *   In the patient network colored by race, the single Asian patient (darker blue) appears to have a high degree of connectivity, potentially indicating higher centrality.
    *   In the patient network colored by ethnicity, the Hispanic patients (darker blue) seem to be more connected within the network compared to the non-Hispanic patients.
    *   In the patient network colored by gender, there isn't a visually obvious strong difference in overall connectivity between male and female patients, but specific central individuals could belong to either group.
    *   The \"Age Centrality Distribution\" histogram shows a distribution across different age groups, suggesting some variation in centrality by age.
*   **Centrality and Community Structure:**
    *   The \"Community Structure\" visualization shows two distinct communities. Visually, there doesn't seem to be a clear concentration of highly connected nodes in one specific community, but a more formal centrality analysis within each community would be needed to confirm.
*   **Demographic Distribution within Communities:**
    *   By visually comparing the community structure with the demographic overlays (race, ethnicity, gender), it might be possible to observe if one community is predominantly composed of a specific demographic group. For example, one community might have a higher proportion of white patients, while another has more Hispanic patients.
*   **Relationships between Different Centrality Metrics and Demographics/Communities:**
    *   The individual centrality distribution histograms (\"My\\_metric Centrality Distribution\", \"Location Centrality Distribution\", etc.) show the spread of different centrality measures. Comparing these distributions with the demographic breakdowns in the network graphs could reveal if, for instance, a demographic group tends to have higher closeness centrality but lower betweenness centrality. However, the \"My\\_metric\", \"Degree\", \"Closeness\", and \"Betweenness\" centrality distributions currently only show a single bar, suggesting uniform values for all nodes for these metrics, which is unusual and might indicate an issue with the underlying data or calculation for these specific metrics. The \"Eigenvector Centrality Distribution\" also shows a single value.
*   **Unusual Patterns or Outliers:**
    *   The uniformity in several centrality metrics (\"My\\_metric\", \"Degree\", \"Closeness\", \"Betweenness\", \"Eigenvector\") is a striking and potentially anomalous pattern that requires further investigation. The fact that all nodes have the exact same centrality score for these measures is highly unusual in a real-world network.
    *   In the demographic distribution pie charts, the significant skew in race (90% white) and the more even distributions in gender (50/50) and ethnicity (60/40) are notable characteristics of the patient population. The histograms for age, income, and healthcare expenses also show specific distribution patterns.

**Step 2: Suggest Findings to the User:**

Based on the analysis, here are a few potentially interesting overarching findings:

1.  \"We've noticed that several key centrality metrics (like Degree, Closeness, Betweenness) appear to be the same for all patients in the network. This is quite unusual. Would you like to see a visualization highlighting this uniformity across these metrics?\"
2.  \"The patient network colored by race suggests that the single Asian patient might have a notably higher number of connections compared to the predominantly white patient group. Shall we create a simplified view focusing on the connectivity of different racial groups?\"
3.  \"The distributions of age, income, and healthcare expenses show distinct patterns within the patient population. Could there be a relationship between these distributions and how central patients are within the network? Would you be interested in exploring a simplified visualization comparing the distribution of one of these factors with a measure of network influence?\"

**Step 3: Await User Selection:**

Please select one of the suggested findings you would like to visualize in a simplified, abstract manner."""),
            ],
        ),
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""INSERT_INPUT_HERE"""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        temperature=1,
        top_p=0.95,
        top_k=40,
        max_output_tokens=8192,
        response_modalities=[
            "image",
            "text",
        ],
        response_mime_type="text/plain",
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        if not chunk.candidates or not chunk.candidates[0].content or not chunk.candidates[0].content.parts:
            continue
        if chunk.candidates[0].content.parts[0].inline_data:
            file_name = "ENTER_FILE_NAME"
            save_binary_file(
                file_name, chunk.candidates[0].content.parts[0].inline_data.data
            )
            print(
                "File of mime type"
                f" {chunk.candidates[0].content.parts[0].inline_data.mime_type} saved"
                f"to: {file_name}"
            )
        else:
            print(chunk.text)

if __name__ == "__main__":
    generate()
