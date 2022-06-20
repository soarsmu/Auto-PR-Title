FROM continuumio/miniconda3

WORKDIR /app

COPY environment.yml .

RUN conda env create -f environment.yml
RUN conda init bash
RUN echo "source activate pr-title-generator" > ~/.bashrc

COPY src/ .
WORKDIR /app/src

EXPOSE 8080
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "pr-title-generator", "streamlit", "run", "app.py", "--server.port", "8080"]
