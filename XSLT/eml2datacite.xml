<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:dc="http://purl.org/dc/elements/1.1/"
    xmlns:dcterms="http://purl.org/dc/terms/"
    xmlns:eml="https://eml.ecoinformatics.org/schema/"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:orcid="http://www.orcid.org/ns/orcid"
    xmlns:datacite="https://schema.datacite.org/meta/kernel-4/"
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">


  <xsl:output method="xml" indent="yes" encoding="UTF-8"/>

  <!-- ルートのemlにマッチ -->
  <xsl:template match="/eml:eml">
        <!-- ここにDataCite形式への変換ロジックを記述 -->
    <resource xmlns="https://schema.datacite.org/meta/kernel-4/">

  <!-- Descriptive metadataの記述 -->
      <!-- (DOI　や ) datacite:identifier -->
      <!--→ EML の alternateIdentifier を DOI の値にしています。-->
      <identifier identifierType="DOI">
        <xsl:value-of select="eml:dataset/eml:alternateIdentifier"/>
      </identifier>

      <!-- datacite:creators --> 
      <creators>
        <xsl:for-each select="eml:dataset/eml:creator">
          <creator>
            <creatorName>
              <xsl:value-of select="eml:individualName/eml:givenName" />
              <xsl:text> </xsl:text>
              <xsl:value-of select="eml:individualName/eml:surName" />
            </creatorName>
            <xsl:if test="eml:organizationName">
              <affiliation>
                <xsl:value-of select="eml:organizationName"/>
              </affiliation>
            </xsl:if>
          </creator>
        </xsl:for-each>
      </creators>

      <!-- datacite:title -->
      <titles>
        <title>
          <xsl:value-of select="eml:dataset/eml:title" />
        </title>
      </titles>

      <!-- datacite:publisher -->
      <publisher>
        <xsl:choose>
          <xsl:when test="eml:dataset/eml:publisher/eml:individualName">
            <xsl:value-of select="eml:dataset/eml:publisher/eml:individualName/eml:givenName"/>
            <xsl:text> </xsl:text>
            <xsl:value-of select="eml:dataset/eml:publisher/eml:individualName/eml:surName" />
          </xsl:when>
          <xsl:otherwise>
            <xsl:value-of select="eml:dataset/eml:publisher/eml:organizationName"/>
          </xsl:otherwise>
        </xsl:choose>
      </publisher>

      <!-- datacite:publicationYear -->
      <!-- pubDate の最初4文字＝ 年 の部分を抽出しています。-->
      <publicationYear>
        <xsl:value-of select="substring(eml:dataset/eml:pubDate,1,4)"/>
      </publicationYear>

      <!-- datacite:resourceType -->
      <!-- 一律に Dataset としています。-->
      <resourceType resourceTypeGeneral="Dataset">Dataset</resourceType>

    </resource>
  </xsl:template>

</xsl:stylesheet>
