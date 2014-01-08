import solr
import sys

def main():
    print "Emptying Solr"
    solrconn = solr.SolrConnection("http://localhost:8080/goudimel-solr")
    solrconn.delete_query("*:*")
    solrconn.commit()



if __name__ == "__main__":
    main()
    sys.exit()