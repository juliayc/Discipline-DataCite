# Discipline-DataCite
(英語)
This project aims to support metadata interoperability between domain-specific formats (like EML) and DataCite metadata schema, in order to enhance dataset findability and reuse.
Through this project, we explore the feasibility and applicability of converting various domain-specific metadata formats to DataCite metadata schema.
We promote the use of the six mandatory items defined by DataCite as a common minimum standard for metadata annotation.
This repository provides a collection of XSLT stylesheets for transforming disciplinary metadata into the DataCite metadata schema. 

(日本語)
本プロジェクトは、EMLなどの分野別メタデータからDataCiteメタデータスキーマへの互換性を検討し、研究データの発見性と再利用性を高めることを目的としています。
本プロジェクトを通じて、さまざまな分野特有のメタデータ形式をDataCiteに変換する際の可能性と実用性を検討しています。
また、DataCiteメタデータスキーマにおける6つの必須項目を、共通の最小標準の記述メタデータとして推奨しています。
このリポジトリは、分野別メタデータを DataCite メタデータスキーマに変換するための XSLT スタイルシート集を提供します。

# XSLT Stylesheets　（Update 2025-06-28）
- `EML2datacite.xslt`: Converts EML metadata to DataCite format.
- `EML2datacite.xslt`: EML メタデータを DataCite 形式に変換します。
- 
# Project Structure
discipline-datacite/
├── README.md
├── LICENSE
├── xslt/
│ └── eml-to-datacite.xslt
├── eml.examples/
Feel free to submit issues or pull requests if you'd like to add support for additional metadata formats or improve the current stylesheets.

#
This work was partially supported by the "Project for Building a Research Data Ecosystem Promoting the Use of AI and Related Technologies."
If you have any questions or inquiries, please feel free to contact us at cong.y@nagoya-u.jp.

本研究の一部は、「AI等の活用を推進する研究データエコシステム構築事業」からの助成を受けて実施されました。
ご質問やご不明な点がございましたら、どうぞお気軽に cong.y@nagoya-u.jp までご連絡ください。


