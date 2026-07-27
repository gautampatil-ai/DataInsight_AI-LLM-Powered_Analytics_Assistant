import pandas as pd
import numpy as np
import re

class LocalAIAssistant:
    """Keyless AI Data Assistant using local statistical parsing and rules."""
    
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def parse_query(self, query: str) -> dict:
        q = query.lower().strip()
        num_cols = self.df.select_dtypes(include=[np.number]).columns.tolist()
        cat_cols = self.df.select_dtypes(exclude=[np.number]).columns.tolist()

        # 1. Average / Mean Query
        if "average" in q or "mean" in q:
            for col in num_cols:
                if col.lower() in q:
                    avg_val = self.df[col].mean()
                    return {
                        "text": f"The average value for **{col}** is **{avg_val:,.2f}**.",
                        "code": f"df['{col}'].mean()",
                        "chart_type": None
                    }

        # 2. Missing values Query
        if "missing" in q or "null" in q:
            nulls = self.df.isna().sum()
            nulls_found = nulls[nulls > 0]
            if nulls_found.empty:
                return {"text": "No missing values found in the dataset!", "code": "df.isna().sum()", "chart_type": None}
            else:
                summary = "\n".join([f"- **{k}**: {v} missing" for k, v in nulls_found.items()])
                return {"text": f"Found missing values:\n{summary}", "code": "df.isna().sum()", "chart_type": None}

        # 3. Top Records / Aggregation
        if "highest" in q or "top" in q:
            for cat in cat_cols:
                for num in num_cols:
                    if cat.lower() in q or num.lower() in q:
                        res = self.df.groupby(cat)[num].sum().sort_values(ascending=False).reset_index()
                        top_item = res.iloc[0]
                        return {
                            "text": f"**{top_item[cat]}** has the highest total **{num}** ({top_item[num]:,.2f}).",
                            "code": f"df.groupby('{cat}')['{num}'].sum().sort_values(ascending=False)",
                            "chart_type": "bar",
                            "data": res.head(10),
                            "x": cat,
                            "y": num
                        }

        # 4. Correlation Query
        if "correlation" in q or "correlated" in q:
            if len(num_cols) >= 2:
                corr = self.df[num_cols].corr()
                unstack_corr = corr.unstack()
                unstack_corr = unstack_corr[unstack_corr < 1.0].sort_values(ascending=False)
                top_pair = unstack_corr.index[0]
                val = unstack_corr.iloc[0]
                return {
                    "text": f"Strongest correlated pair is **{top_pair[0]}** and **{top_pair[1]}** (r = {val:.2f}).",
                    "code": f"df[{num_cols}].corr()",
                    "chart_type": "heatmap"
                }

        # Fallback automated summary insight
        return {
            "text": f"Dataset contains **{len(self.df):,} rows** and **{len(self.df.columns)} columns** ({len(num_cols)} numeric, {len(cat_cols)} categorical).",
            "code": "df.info()",
            "chart_type": None
        }
