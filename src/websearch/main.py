#!/usr/bin/env python
import sys
import warnings

from crew import Websearch
from datetime import datetime
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'query': 'Can you give me some really interesting and non-conventional facts about our universe?',
        "date": datetime.now().strftime("%Y-%m-%d")
    }
    Websearch().crew().kickoff(inputs=inputs)


run()
