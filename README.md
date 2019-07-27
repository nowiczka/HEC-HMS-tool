# HEC HMS tool for real time flood forecasting 

This repository contains didactic examples of a management of HEC-HMS in batch mode; and presents data analysis automation, and flood warning system in form of a tool for a real time flood forecasting using Jython Scripts. This tool based on HEC-HMS is investigated by scripting between HEC-DSSVue (Java application which uses Jython), Anaconda (Python distribution) using Py4J (one of Python packages enables Python programs to dynamically access arbitrary Java objects), and shell scripting.

Generally, the tool aims to conduct specified simulation, in a specified flood model by HEC-HMS after introducing new 24 hours rainfall data in text files and send alerts about flow rates via email. Simultaneously, it allows prediction of a basin response quickly and issue a warning about a certain danger related to the peak flows. This alert can be used to manage operations of a reservoir coupled with flood
models, to prepare a zone for emergency response to a flood event.
