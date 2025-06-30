import glob
import os
import subprocess

xslname = 'spase2jpcoar2_0.xsl'
input_xml = "spase.xml"
output_xml = "eml_datacite_output.xml"

def convert_single(xsl_path, input_path, output_path):
    cmd = f'xsltproc "{xsl_path}" "{input_path}"'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        proc = subprocess.Popen(cmd, stdout=f, stderr=subprocess.PIPE, shell=True)
        errmsg = proc.stderr.read()
        if errmsg:
            print(f"Error in converting '{input_path}':")
            for line in errmsg.decode('utf-8').splitlines():
                print(f"  {line}")
        else:
            print(f"Converted '{input_path}' -> '{output_path}'")

def convert_batch(xsl_path, cwd):
    targets = glob.glob("DisplayData/**/*.xml", recursive=True) + \
              glob.glob("NumericalData/**/*.xml", recursive=True)
    if not targets:
        print("No XML files found in DisplayData/ or NumericalData/")
        return

    for target in targets:
        out_xml = os.path.join('jpcoar', target)
        convert_single(xsl_path, target, out_xml)

if __name__ == '__main__':
    cwd = os.getcwd()
    xsl_path = os.path.join(cwd, xslname)

    if not os.path.exists(xsl_path):
        print(f"XSL file not found: {xsl_path}")
        exit(1)

    # 先尝试批量转换（如果有符合条件的文件）
    print("\nStarting single file conversion...")
    convert_batch(xsl_path, input_xml, output_xml)

    # 如果你只想转换单个文件，取消下面注释即可：
    # print("\nStarting single file conversion...")
    # convert_single(xsl_path, input_xml, output_xml)
