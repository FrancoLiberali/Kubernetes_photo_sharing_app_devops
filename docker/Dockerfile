FROM python
RUN mkdir -p data/
WORKDIR data/
COPY file1.html file1.html
COPY file2.html file2.html
COPY file3.html file3.html
EXPOSE 8080
CMD ["python3", "-m", "http.server", "8080"]

