vindula.chat
============

Vindula Chat

Produto de chat xmpp

Instalação
	* dependencia
		OpenFire >= 3.7.1
		
		
		configuração ngnix
		
			location /http-bind {
	            proxy_pass http://localhost:7070/http-bind/;
	        }
	
	        location ^~ /http-user/ {
		    rewrite ^/http-user/(.*) /$1 break;
	            proxy_pass http://localhost:9090/;
	        }
		
	* buildout
		egg = 
			  vindula.chat
	
		zcml =
			  vindula.chat
	
		[instance]
		
			zcml-additional =
			  <configure xmlns="http://namespaces.zope.org/zope">
			    <include package="jarn.xmpp.twisted" file="reactor.zcml" />
			  </configure>
			  
	* Cofigurar a conexão com o banco de dados no arquivo configure.zcml
		<store
	  		name="openfire"
	  		uri="mysql://root:root@localhost/openfire" />
