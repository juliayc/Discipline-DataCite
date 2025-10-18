<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:tei="http://www.tei-c.org/ns/1.0"
    xmlns:datacite="http://datacite.org/schema/kernel-4"
    exclude-result-prefixes="tei">

  <xsl:output method="xml" indent="yes" encoding="UTF-8"/>

  <xsl:template match="/tei:TEI">
    <resource xmlns="http://datacite.org/schema/kernel-4">
      
      <identifier identifierType="DOI">
        <xsl:value-of select="tei:teiHeader/tei:fileDesc/tei:publicationStmt/tei:idno"/>
      </identifier>

      <creators>
        <xsl:for-each select="tei:teiHeader/tei:fileDesc/tei:titleStmt/tei:author">
          <creator>
            <creatorName>
              <xsl:value-of select="."/>
            </creatorName>
          </creator>
        </xsl:for-each>
      </creators>

      <titles>
        <title>
          <xsl:value-of select="tei:teiHeader/tei:fileDesc/tei:titleStmt/tei:title"/>
        </title>
      </titles>

      <publisher>
        <xsl:value-of select="tei:teiHeader/tei:fileDesc/tei:publicationStmt/tei:publisher"/>
      </publisher>

      <publicationYear>
        <xsl:value-of select="substring(tei:teiHeader/tei:fileDesc/tei:publicationStmt/tei:date/@when, 1, 4)"/>
      </publicationYear>

      <resourceType resourceTypeGeneral="Text">
        <xsl:value-of select="tei:teiHeader/tei:profileDesc/tei:textClass/tei:keywords"/>
      </resourceType>

    </resource>
  </xsl:template>

</xsl:stylesheet>
