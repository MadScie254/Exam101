#!/usr/bin/env python3
"""
PDF Export Script for TB Burden Analysis Notebook
Alternative method for converting Jupyter notebook to PDF when nbconvert has issues
"""

import subprocess
import sys
import os
from pathlib import Path

def export_notebook_to_pdf():
    """
    Convert Jupyter notebook to PDF using alternative methods
    """
    notebook_path = "notebooks/TB_Burden_Report.ipynb"
    output_dir = "report"
    output_name = "MCSC2108_TB_Burden_Report"
    
    # Ensure output directory exists
    Path(output_dir).mkdir(exist_ok=True)
    
    print("TB Burden Analysis - PDF Export")
    print("=" * 50)
    
    # Method 1: Try nbconvert with HTML intermediate
    try:
        print("Attempting HTML conversion...")
        cmd_html = [
            sys.executable, "-m", "jupyter", "nbconvert",
            "--to", "html",
            "--output-dir", output_dir,
            "--output", output_name,
            notebook_path
        ]
        
        result = subprocess.run(cmd_html, capture_output=True, text=True, timeout=60)
        
        if result.returncode == 0:
            html_file = os.path.join(output_dir, f"{output_name}.html")
            print(f"✓ HTML conversion successful: {html_file}")
            
            # Try to convert HTML to PDF using weasyprint
            try:
                print("Attempting PDF conversion with weasyprint...")
                import weasyprint
                
                pdf_file = os.path.join(output_dir, f"{output_name}.pdf")
                weasyprint.HTML(filename=html_file).write_pdf(pdf_file)
                print(f"✓ PDF conversion successful: {pdf_file}")
                return True
                
            except ImportError:
                print("⚠ weasyprint not available")
            except Exception as e:
                print(f"⚠ weasyprint conversion failed: {e}")
        
        else:
            print(f"❌ HTML conversion failed: {result.stderr}")
    
    except subprocess.TimeoutExpired:
        print("❌ Conversion timed out")
    except Exception as e:
        print(f"❌ Conversion error: {e}")
    
    # Method 2: Direct PDF conversion
    try:
        print("\nAttempting direct PDF conversion...")
        cmd_pdf = [
            sys.executable, "-m", "jupyter", "nbconvert",
            "--to", "pdf",
            "--output-dir", output_dir,
            "--output", output_name,
            notebook_path
        ]
        
        result = subprocess.run(cmd_pdf, capture_output=True, text=True, timeout=120)
        
        if result.returncode == 0:
            pdf_file = os.path.join(output_dir, f"{output_name}.pdf")
            print(f"✓ Direct PDF conversion successful: {pdf_file}")
            return True
        else:
            print(f"❌ Direct PDF conversion failed: {result.stderr}")
    
    except Exception as e:
        print(f"❌ Direct conversion error: {e}")
    
    # Fallback instructions
    print("\n" + "=" * 50)
    print("MANUAL EXPORT INSTRUCTIONS")
    print("=" * 50)
    print("1. Open the notebook in Jupyter:")
    print("   jupyter notebook notebooks/TB_Burden_Report.ipynb")
    print("2. Use File → Download as → PDF via LaTeX")
    print("3. Or: File → Print → Save as PDF in browser")
    print("4. Save to report/ directory as MCSC2108_TB_Burden_Report.pdf")
    
    html_file = os.path.join(output_dir, f"{output_name}.html")
    if os.path.exists(html_file):
        print(f"\nHTML version available: {html_file}")
        print("You can print this to PDF from your browser")
    
    return False

if __name__ == "__main__":
    success = export_notebook_to_pdf()
    sys.exit(0 if success else 1)