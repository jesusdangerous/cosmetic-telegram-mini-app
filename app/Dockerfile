FROM maven:3.9.6-eclipse-temurin-21 AS build
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline
COPY src ./src
RUN mvn package -DskipTests

ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ENV MAIL_NAME=${MAIL_NAME}
ENV MAIL_PASSWORD=${MAIL_PASSWORD}

FROM eclipse-temurin:21-jdk-jammy
WORKDIR /app
COPY --from=build /app/target/app-0.0.1-SNAPSHOT.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
