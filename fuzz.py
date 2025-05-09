from hypothesis import given, strategies as st
import parser
import scanner
import graphtaint
import main
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("fuzz_logger")

@given(st.text())
def test_loadMultiYAML(input_str):
    try:
        with open("temp.yaml", "w") as f:
            f.write(input_str)
        result = parser.loadMultiYAML("temp.yaml")
        logger.info(f"loadMultiYAML returned {len(result)} dicts.")
    except Exception as e:
        logger.error(f"Error in loadMultiYAML: {e}")

@given(st.dictionaries(st.text(), st.text(), max_size=5), st.text())
def test_getValsFromKey(dictionary, target):
    try:
        list_holder = []
        parser.getValsFromKey(dictionary, target, list_holder)
        logger.info(f"Found {len(list_holder)} values for key {target}.")
    except Exception as e:
        logger.error(f"Error in getValsFromKey: {e}")

@given(st.dictionaries(st.text(), st.text(), max_size=5))
def test_scanForSecrets(dictionary):
    try:
        result = scanner.scanForSecrets(dictionary)
        logger.info(f"Secrets found in {len(result)} keys.")
    except Exception as e:
        logger.error(f"Error in scanForSecrets: {e}")

@given(st.lists(st.tuples(st.text(), st.text(), st.lists(st.text(), min_size=0), st.lists(st.text(), min_size=0), st.lists(st.text(), min_size=0), st.dictionaries(st.text(), st.text(), max_size=3), st.dictionaries(st.text(), st.text(), max_size=3), st.dictionaries(st.text(), st.text(), max_size=3), st.dictionaries(st.text(), st.text(), max_size=3), st.dictionaries(st.text(), st.text(), max_size=3), st.dictionaries(st.text(), st.text(), max_size=3), st.dictionaries(st.text(), st.text(), max_size=3), st.dictionaries(st.text(), st.text(), max_size=3), st.dictionaries(st.text(), st.text(), max_size=3), st.dictionaries(st.text(), st.text(), max_size=3), st.dictionaries(st.text(), st.text(), max_size=3), st.dictionaries(st.text(), st.text(), max_size=3), st.dictionaries(st.text(), st.text(), max_size=3), st.dictionaries(st.text(), st.text(), max_size=3), st.dictionaries(st.text(), st.text(), max_size=3), st.booleans(), st.booleans())))
def test_getCountFromAnalysis(input_data):
    try:
        result = main.getCountFromAnalysis(input_data)
        logger.info(f"Analysis returned {len(result)} entries.")
    except Exception as e:
        logger.error(f"Error in getCountFromAnalysis: {e}")

@given(st.text(), st.dictionaries(st.text(), st.text(), max_size=5))
def test_mineSecretGraph(path, dictionary):
    try:
        result = graphtaint.mineSecretGraph(path, dictionary, {"test": [("secret",)]})
        logger.info(f"mineSecretGraph result: {result}")
    except Exception as e:
        logger.error(f"Error in mineSecretGraph: {e}")
