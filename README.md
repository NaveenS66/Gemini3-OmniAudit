# 🛡️ Omni-Audit: Next-Gen Multimodal Logic Engine
**Built for the Google Gemini 3 Hackathon**

## 🚀 The Vision
Most AI applications focus on simple recognition (OCR) or basic chat. **Omni-Audit** pushes the boundaries of the **Gemini 3 Reasoning Kernel** to perform "Contextual Auditing." It identifies logical fallacies, temporal anachronisms, and physical safety risks that standard AI models overlook.

## 🧠 Key Features (Powered by Gemini 3)
- **Temporal Reasoning:** Identifies date/time conflicts in administrative documents (e.g., catching batch errors in university circulars).
- **Physical Safety Logic:** Understands the "cause-and-effect" of physical hazards, such as the dangers of daisy-chaining electrical outlets.
- **Mechanical/Structural Logic:** Detects lethal mechanical errors (e.g., improper car jack placement) by reasoning about material physics and intent.
- **UX/Design Audit:** Identifies violations of human mental models in spatial design (e.g., illogical elevator button layouts).

## 🛠️ Technical Stack
- **Model:** `gemini-3-flash-preview` (v1beta API)
- **Interface:** Streamlit (Python)
  
## 📖 How to Run
1. Clone the repository: `git clone https://github.com/NaveenS66/Gemini3-OmniAudit`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `streamlit run app.py`
4. The app will prioritize Streamlit Secrets; otherwise, enter your Gemini API Key in the sidebar.

## 🏆 Why Gemini 3?
Omni-Audit relies on the **Advanced Reasoning Kernels** unique to the Gemini 3 family. Previous models could identify objects but often failed to link them logically to safety standards or future-dated events. Gemini 3 provides the "System 2" thinking necessary for high-stakes auditing.
