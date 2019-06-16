test on localhost deploy

1. Build and run frontend - docker build -t web-frontend .
    docker run --rm -p 88:80 web-frontend
    
2. Build and run backend - docker build -t web-backend .
    docker run --rm -p 8080:8080 web-backend