
def Summary(pdftext,apikey):
    openai.api_key = apikey
    engine_list = openai.Engine.list()  # calling the engines available from the openai api
    for page in pdftext:
        text = page.extract_text()
        response = openai.Completion.create(engine="davinci", prompt=text, temperature=0.3,
                                            max_tokens=140,
                                            top_p=1,
                                            frequency_penalty=0,
                                            presence_penalty=0,
                                            stop=["\n"]
                                            )
        print(response["choices"][0]["text"])
if __name__ == "__main__":
    import openai
    import pdfplumber
    file = "C:/Users/kickass/Downloads/N.D. Lewis - Neural Networks for Time Series Forecasting with R-N.D. Lewis (2017).pdf"
    apifile ="C:/Users/kickass/Dropbox/openapikey.bin"
    with open(apifile, encoding="utf-8") as binary_file:
        # Read the whole file at once
        apikey = binary_file.read()
    pdftext = pdfplumber.open(file).pages
    Summary(pdftext,str(apikey))
