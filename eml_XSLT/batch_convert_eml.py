import os
import subprocess
import shutil

# ファイル名定義
xsl_file = "eml2datacite.xsl"
input_xml = "eml_example.xml"
output_xml = "eml_datacite_output.xml"


def check_xsltproc():
    """xsltproc が使えるか確認"""
    return shutil.which("xsltproc") is not None


def transform_eml_to_datacite(xsl, input_xml, output_xml):
    #     """EMLをDataCite形式へ変換""" 絶対パス取得（必要なら）
    cwd = os.getcwd()
    
    xsl_path = os.path.join(cwd, xsl)
    input_path = os.path.join(cwd, input_xml)
    output_path = os.path.join(cwd, output_xml)



    if not os.path.exists(xsl_path):
        print(f"❌ XSLファイルが見つかりません: {xsl_path}")
        return

    if not os.path.exists(input_path):
        print(f"❌ 入力XMLファイルが見つかりません: {input_path}")
        return

    if not check_xsltproc():
        print("❌ xsltproc が見つかりません。macOS の場合、以下でインストールできます：")
        print("   brew install libxslt")
        return

    # xsltproc コマンド構築
    cmd = ["xsltproc", xsl_path, input_path]

    try:
        # 出力ファイルに書き込み
        with open(output_path, "w", encoding ="utf-8") as f_out:
            proc = subprocess.Popen(
                cmd,
                stdout=f_out,
                stderr=subprocess.PIPE
            )
            _, stderr = proc.communicate()

            # エラーがあれば表示
            if proc.returncode != 0:
                print("変換エラーが発生しました。")
                print(stderr.decode("utf-8"))
            else:
                print(f"変換成功！ → {output_path}")
                                # オプションで最初の数行表示
                with open(output_path, encoding="utf-8") as f:
                    print("--- 出力プレビュー（先頭5行） ---")
                    for i in range(5):
                        line = f.readline()
                        if not line:
                            break
                        print(line.strip())


    except Exception as e:
        print(f"❌ 予期しないエラー: {e}")

if __name__ == "__main__":
    transform_eml_to_datacite(xsl_file, input_xml, output_xml)












