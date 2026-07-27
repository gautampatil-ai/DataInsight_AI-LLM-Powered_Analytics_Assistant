import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
import pandas as pd
import config

class ReportGenerator:
    """Generates PDF reports locally without API keys."""
    
    @staticmethod
    def generate_pdf(df: pd.DataFrame, filename: str = "summary_report.pdf") -> str:
        filepath = config.REPORTS_DIR / filename
        doc = SimpleDocTemplate(str(filepath), pagesize=letter)
        styles = getSampleStyleSheet()
        
        elements = []
        
        # Header Title
        title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontSize=20, textColor=colors.HexColor('#7C3AED'))
        elements.append(Paragraph("Data Analysis & Executive Report", title_style))
        elements.append(Spacer(1, 12))
        
        # Summary Overview
        elements.append(Paragraph(f"<b>Total Dataset Records:</b> {len(df):,}", styles['Normal']))
        elements.append(Paragraph(f"<b>Total Features/Columns:</b> {len(df.columns)}", styles['Normal']))
        elements.append(Paragraph(f"<b>Missing Values Total:</b> {df.isna().sum().sum():,}", styles['Normal']))
        elements.append(Spacer(1, 18))
        
        # Sample Data Table
        elements.append(Paragraph("<b>Sample Preview (Top 5 Rows):</b>", styles['Heading2']))
        elements.append(Spacer(1, 8))
        
        preview_data = [df.columns.tolist()[:5]] + df.iloc[:5, :5].values.tolist()
        table = Table(preview_data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2563EB')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey)
        ]))
        
        elements.append(table)
        doc.build(elements)
        return str(filepath)
