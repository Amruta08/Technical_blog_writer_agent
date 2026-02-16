
## Technical Blog writer agent
<p>Technical Blog writing agent with planning, research and image generation functionality.</p>
<p><b>Live Demo:</b>https://technicalblogwriteragent-8qy8obrm85whkitcrszdfu.streamlit.app/</p>
<hr/>

### Progam Ouput :-
<h4> Blog Title Input :-</h4>
<img width="1899" height="723" alt="image" src="https://github.com/user-attachments/assets/a53a73a6-d1d4-4f15-9125-1f94544a71c6" />

<h4> Blog Output :- (With images and codes at relevant places)</h4>
<img width="1889" height="712" alt="image" src="https://github.com/user-attachments/assets/98404c40-67ef-4d75-b785-dc52a393ecd9" />
<img width="1889" height="749" alt="image" src="https://github.com/user-attachments/assets/b7844ae3-b6b8-4ac1-b706-cf9b22c6c140" />
<img width="1823" height="774" alt="image" src="https://github.com/user-attachments/assets/8225482a-b1df-430d-96ce-36ce73ae7e2f" />
<hr/>

### 🛠️ Tech Stack :-

- Python
- LangChain + LangGraph
- OpenAI API
- Google Gemini (Image Generation)
- Tavily Search API
- Pydantic
- SQLite
- Streamlit
<hr/>

### 🏗️ Architecture Overview :-
1. Router Node
   - Decides whether web research is required
   - Classifies into closed-book, hybrid and open-book modes
2. Research Node
   - Uses Tavily API for web search
   - Synthesizes evidence into structured objects
3. Orchestrator Node
   - Generates structured blog plan (5-9 sections)
   - Adapts depth based on audience level
4. Worker Nodes
   - Generates each blog session independently
5. Reducer Subgraph
   - Merges sections
   - Decides images
   - Generates and embeds images
   - Produces final Markdown output

<hr/>

### 🔄 Workflow diagram :-
<img width="160" height="630" alt="image" src="https://github.com/user-attachments/assets/912f61f7-93aa-482d-9ade-d3ea6d78f4d3" />

