
from setuptools import setup, find_packages
setup(
    name="shauffeur",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["pyyaml"],
    entry_points={
        "console_scripts": [
            "shauffeur_node=shauffeur.ros2.shauffeur_node:main",
        ]
    }
)
