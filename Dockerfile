FROM tomcat:9.0-jre8-alpine

LABEL maintainer="isantosp@protonmail.com"

ADD sample.war /usr/local/tomcat/webapps/

EXPOSE 8080

CMD ["catalina.sh", "run"]
