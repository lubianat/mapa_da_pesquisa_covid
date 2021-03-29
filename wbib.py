import os
import glob
import urllib.parse
import pandas as pd
import unicodedata

def render_dashboard():


  url1 = get_query_url_for_articles()
  url3 = get_topics_as_table()
  url4 = get_query_url_for_venues()
  url5 = get_query_url_for_locations()
  url7 = get_query_url_for_authors()

  html = """
<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Mapa da Pesquisa: COVID-19</title>
  <meta property="og:description" content="powered by Wikidata">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
  <link href="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js" rel="stylesheet"
    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.8.2/css/bulma.min.css">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
</head>

<body>
  <section class="section">
    <div class="container">
      <div class="columns is-centered">
        <div class="column is-half has-text-centered">
          <h1 class="title is-1"> Mapa da Pesquisa: COVID-19</h1>
          <h2>A ciência de brasileiros e brasileiras contra a pandemia</h2>
        </div>
      </div>
    </div>
    <div class="column is-half has-text-centered">
  </section>
  <div class="columns is-centered">
    <div class="tabs is-centered">
      <ul>
        <li id="one-tab" class="">
          <a onclick="switchToOne()">
            <span>Artigos</span>
          </a>
        </li>
        <li id="three-tab">
          <a onclick="switchToThree()">
            <span>Temas (lista)</span>
          </a>
        </li>
        <li id="four-tab">
          <a onclick="switchToFour()">
            <span>Revistas</span>
          </a>
        </li>
        <li id="five-tab">
          <a onclick="switchToFive()">
            <span>Autores (mapa)</span>
          </a>
        <li id="seven-tab">
          <a onclick="switchToSeven()">
            <span>Autores (lista)</span>
          </a>
        </li>
      </ul>
      <!--/tabs is-centered-->
    </div>
  </div>
  </div>
  </section>
  <div class="container">
    <div id="one-tab-content">
      <h5 class="title is-5" style="text-align:center;"> 100 artigos mais recentes com pé no Brasil </h5>
          <iframe width=92% height="500" src=""" + '"'+ url1 +'"' + """></iframe>
    </div>
    <div class="is-hidden" id="five-tab-content">
      <h5 class="title is-5" style="text-align:center;"> Mapa das instituições no território nacional </h5>
            <iframe width=92% height="500" src=""" + '"'+ url5 +'"' + """></iframe>
    </div>
    <div class="is-hidden" id="seven-tab-content">
      <h5 class="title is-5" style="text-align:center;"> Autores dos artigos, por número de publicações sobre o tema </h5>
        <iframe width=92% height="500" src=""" + '"'+ url7 +'"' + """></iframe>
      </div>
    <div class="is-hidden" id="three-tab-content">
      <h5 class="title is-5" style="text-align:center;"> Top 100 tópicos relacionados  </h5>
            <iframe width=92% height="500" src=""" + '"'+ url3+'"' + """></iframe>
    </div>
    <div class="is-hidden" id="four-tab-content">
      <h5 class="title is-5" style="text-align:center;"> Revistas nas quais esses artigos foram publicados</h5>
            <iframe width=92% height="500" src=""" + '"'+ url4 +'"' + """></iframe>
    </div>


  </div>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script>

    function switchToOne() {
      removeActive();
      hideAll();
      $("#one-tab").addClass("is-active");
      $("#one-tab-content").removeClass("is-hidden");
    }

    function switchToThree() {
      removeActive();
      hideAll();
      $("#three-tab").addClass("is-active");
      $("#three-tab-content").removeClass("is-hidden");
    }

    function switchToFour() {
      removeActive();
      hideAll();
      $("#four-tab").addClass("is-active");
      $("#four-tab-content").removeClass("is-hidden");
    }

    function switchToFive() {
      removeActive();
      hideAll();
      $("#five-tab").addClass("is-active");
      $("#five-tab-content").removeClass("is-hidden");
    }

    function switchToSeven() {
      removeActive();
      hideAll();
      $("#seven-tab").addClass("is-active");
      $("#seven-tab-content").removeClass("is-hidden");
    }

    function removeActive() {
      $("li").each(function () {
        $(this).removeClass("is-active");
      });
    }

    function hideAll() {
      $("#one-tab-content").addClass("is-hidden");
      $("#three-tab-content").addClass("is-hidden");
      $("#four-tab-content").addClass("is-hidden");
      $("#five-tab-content").addClass("is-hidden");
      $("#seven-tab-content").addClass("is-hidden");
      $("#eight-tab-content").addClass("is-hidden");
    }

  </script>
  </br>

  <footer class="footer">
    <div class="container">
      <div class="content has-text-centered">
        <p>
          Esse conteúdo está disponível <a href="https://creativecommons.org/publicdomain/zero/1.0/"> sob a licença
            Creative Commons CC0</a>

        <p> Buscas SPARQL adapadtadas da plataforma <a href="https://scholia.toolforge.org/">Scholia</a> </p>
        <p> Dashboard adaptado por <a href="https://www.wikidata.org/wiki/User:TiagoLubiana">TiagoLubiana</a>
          a partir do dashboard <a href="https://wikiproject-india.github.io/covid19dashboard/"> do WikiProjeto COVID-19
            na Índia</a>
        <p> Código do site disponível em <a href="https://github.com/lubianat/mapa_da_pesquisa_covid">
            https://github.com/lubianat/mapa_da_pesquisa_covid </a>. </p>
        </p>
      </div>
    </div>
  </footer>
</body>

</html>
  """
  return(html)


def get_work_selector_for_covid_19():
  selector = """ 
  ?trabalho wdt:P921 wd:Q84263196.
  ?trabalho wdt:P50 ?autor.
  ?autor wdt:P108 | wdt:P1416 ?institution.
  ?institution wdt:P17 wd:Q155.
  """

  return(selector)






def render_url(query):
  return "https://query.wikidata.org/embed.html#" + urllib.parse.quote(query, safe='')
  
def get_query_url_for_articles():
  query = """

  #defaultView:Table
  SELECT
  (MIN(?dates) AS ?date)
  ?trabalho ?trabalhoLabel
  (GROUP_CONCAT(DISTINCT ?tipo_label; separator=", ") AS ?tipo)
  ?revista ?revistaLabel
  (GROUP_CONCAT(DISTINCT ?autor_label; separator=", ") AS ?autores)
  WHERE {
  """ + get_work_selector_for_covid_19() + """
  OPTIONAL {
    ?autor rdfs:label ?autor_label_ . FILTER (LANG(?autor_label_) = 'en')
  }
  BIND(COALESCE(?autor_label_, SUBSTR(STR(?autor), 32)) AS ?autor_label)
  OPTIONAL { ?trabalho wdt:P31 ?tipo_ . ?tipo_ rdfs:label ?tipo_label . FILTER (LANG(?tipo_label) = 'pt') }
  ?trabalho wdt:P577 ?datetimes .
  BIND(xsd:date(?datetimes) AS ?dates)
  OPTIONAL { ?trabalho wdt:P1433 ?revista }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en,da,de,es,fr,jp,no,ru,sv,zh". }  
  }
  GROUP BY ?trabalho ?trabalhoLabel ?revista ?revistaLabel
  ORDER BY DESC(?date)
  LIMIT 100 

  """
  
  return render_url(query)

def get_topics_as_table():
  query_3 = """


  #defaultView:Table
  SELECT ?count ?theme ?themeLabel ?example_work ?example_workLabel
  WITH {
    SELECT (COUNT(?trabalho) AS ?count) ?theme (SAMPLE(?trabalho) AS ?example_work)
    WHERE {
      """ + get_work_selector_for_covid_19() + """
      ?trabalho wdt:P921 ?theme .
    }
    GROUP BY ?theme
  } AS %result
  WHERE {
    INCLUDE %result
    SERVICE wikibase:label { bd:serviceParam wikibase:language "en,da,de,es,fr,jp,nl,no,ru,sv,zh" . } 
  }
  ORDER BY DESC(?count) 
  LIMIT 100

  """
  return render_url(query_3) 

def get_query_url_for_venues():
  query_4 = """
  # Venue statistics for a collection
  SELECT
    ?count (SAMPLE(?short_name_) AS ?short_name)
    ?revista ?revistaLabel
    ?topics ?topicsUrl
  WITH {
    SELECT
      (COUNT(DISTINCT ?trabalho) as ?count)
      ?revista
      (GROUP_CONCAT(DISTINCT ?topic_label; separator=", ") AS ?topics)
    WHERE {
      """ + get_work_selector_for_covid_19() + """
      ?trabalho wdt:P1433 ?revista .
      OPTIONAL {
        ?revista wdt:P921 ?topic .
        ?topic rdfs:label ?topic_label . FILTER(LANG(?topic_label) = 'en') }
    }
    GROUP BY ?revista
  } AS %result
  WHERE {
    INCLUDE %result
    OPTIONAL { ?revista wdt:P1813 ?short_name_ . }
    SERVICE wikibase:label { bd:serviceParam wikibase:language "en,da,de,es,fr,jp,nl,no,ru,sv,zh". }  
  } 
  GROUP BY ?count ?revista ?revistaLabel ?topics ?topicsUrl
  ORDER BY DESC(?count)

  """
  return render_url(query_4) 

def get_query_url_for_locations():
  query_5 = """


  #defaultView:Map
  SELECT ?organization ?organizationLabel ?geo ?count ?layer
  WITH {
    SELECT DISTINCT ?organization ?geo (COUNT(DISTINCT ?trabalho) AS ?count) WHERE {
      """ + get_work_selector_for_covid_19() + """
      ?autor ( wdt:P108 | wdt:P463 | wdt:P1416 ) / wdt:P361* ?organization . 
      ?organization wdt:P625 ?geo .
      ?organization wdt:P17 wd:Q155.
    }
    GROUP BY ?organization ?geo ?count
    ORDER BY DESC (?count)
    LIMIT 2000
  } AS %organizations
  WHERE {
    INCLUDE %organizations
    BIND(IF( (?count < 1), "No results", IF((?count < 2), "1 result", IF((?count < 5), "1 < results ≤ 10", IF((?count < 101), "10 < results ≤ 100", IF((?count < 1001), "100 < results ≤ 1000", IF((?count < 10001), "1000 < results ≤ 10000", "10000 or more results") ) ) ) )) AS ?layer )
    SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }        
  }
  ORDER BY DESC (?count)


  """
  return render_url(query_5)


def get_query_url_for_authors():
  query_7 = """
  #defaultView:Table
  SELECT (COUNT(?trabalho) AS ?count) ?autor ?autorLabel ?orcids  WHERE {
    """ + get_work_selector_for_covid_19() + """
    OPTIONAL { ?autor wdt:P496 ?orcids }
    SERVICE wikibase:label { bd:serviceParam wikibase:language "en,da,de,es,fr,jp,nl,no,ru,sv,zh". }

    }
  GROUP BY ?autor ?autorLabel ?orcids 
  ORDER BY DESC(?count)

  """
  return render_url(query_7)