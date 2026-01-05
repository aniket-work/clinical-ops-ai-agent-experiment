
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

class ClinicalOpsAgent:
    def __init__(self, data_path='clinical_trial_data.csv'):
        self.data_path = data_path
        self.df = None
        self.output_dir = 'output'
        os.makedirs(self.output_dir, exist_ok=True)
        self.load_data()

    def load_data(self):
        if os.path.exists(self.data_path):
            self.df = pd.read_csv(self.data_path)
            # Convert date columns
            if 'Enrollment_Date' in self.df.columns:
                self.df['Enrollment_Date'] = pd.to_datetime(self.df['Enrollment_Date'])
            print(f"✅ Data loaded: {len(self.df)} records.")
        else:
            print(f"❌ Data file not found at {self.data_path}. Please run data_generator.py first.")

    def run(self, query):
        """
        Simulates an LLM agent that interprets natural language queries 
        and generates the appropriate visualization.
        For this PoC, we use keyword matching to completely control the output 
        and ensure high-quality, professional graphs without reliable LLM API access.
        """
        print(f"\n🤖 Agent received query: '{query}'")
        
        # In a real production agent, this would be an LLM call:
        # response = llm.generate_code(query, schema=self.df.columns)
        # exec(response)
        
        # For this experiment/PoC, we map intents to specific visualization functions
        query = query.lower()
        
        if "adverse event" in query or "severity" in query:
            self.plot_adverse_events()
        elif "enrollment" in query or "time" in query or "progress" in query:
            self.plot_enrollment_trend()
        elif "blood pressure" in query or "bp" in query or "vitals" in query:
            self.plot_vitals_distribution()
        elif "age" in query and "gender" in query:
            self.plot_demographics()
        else:
            print("❓ Query not recognized. Identifying best default view...")
            self.plot_demographics()

    def plot_adverse_events(self):
        print("   Creating Adverse Event Severity Distribution Chart...")
        plt.figure(figsize=(10, 6))
        sns.countplot(data=self.df, x='Adverse_Event_Severity', order=['None', 'Mild', 'Moderate', 'Severe'], palette='viridis')
        plt.title('Distribution of Adverse Event Severity', fontsize=16)
        plt.xlabel('Severity Level', fontsize=12)
        plt.ylabel('Count of Patients', fontsize=12)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        
        output_path = f"{self.output_dir}/adverse_events.png"
        plt.savefig(output_path)
        plt.close()
        print(f"   🖼️ Chart saved to {output_path}")

    def plot_enrollment_trend(self):
        print("   Creating Study Enrollment Over Time Chart...")
        # Preprocessing for time series
        enrollment_counts = self.df.set_index('Enrollment_Date').resample('M').size().cumsum()
        
        plt.figure(figsize=(12, 6))
        enrollment_counts.plot(kind='line', marker='o', color='teal', linewidth=2)
        plt.title('Cumulative Study Enrollment Over Time', fontsize=16)
        plt.xlabel('Date', fontsize=12)
        plt.ylabel('Cumulative Patients Enrolled', fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.6)
        
        output_path = f"{self.output_dir}/enrollment_trend.png"
        plt.savefig(output_path)
        plt.close()
        print(f"   🖼️ Chart saved to {output_path}")

    def plot_vitals_distribution(self):
        print("   Analyzing Vitals (Systolic BP) vs Age...")
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=self.df, x='Age', y='Systolic_BP', hue='Gender', alpha=0.6, palette='deep')
        sns.regplot(data=self.df, x='Age', y='Systolic_BP', scatter=False, color='red', line_kws={'label': 'Trend'})
        plt.title('Systolic Blood Pressure vs. Age', fontsize=16)
        plt.xlabel('Age (Years)', fontsize=12)
        plt.ylabel('Systolic BP (mmHg)', fontsize=12)
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.5)
        
        output_path = f"{self.output_dir}/vitals_analysis.png"
        plt.savefig(output_path)
        plt.close()
        print(f"   🖼️ Chart saved to {output_path}")

    def plot_demographics(self):
        print("   Visualizing Demographics...")
        plt.figure(figsize=(10, 6))
        sns.histplot(data=self.df, x='Age', hue='Gender', multiple='stack', palette='pastel', kde=True)
        plt.title('Patient Demographics: Age and Gender Distribution', fontsize=16)
        plt.xlabel('Age', fontsize=12)
        plt.ylabel('Count', fontsize=12)
        
        output_path = f"{self.output_dir}/demographics.png"
        plt.savefig(output_path)
        plt.close()
        print(f"   🖼️ Chart saved to {output_path}")

if __name__ == "__main__":
    agent = ClinicalOpsAgent()
    
    # Simulate User Prompts
    queries = [
        "Show me the progress of patient enrollment over time",
        "Analyze the adverse event severity across the study",
        "Is there a correlation between age and blood pressure?",
        "Give me a breakdown of the patient demographics"
    ]
    
    for q in queries:
        agent.run(q)
