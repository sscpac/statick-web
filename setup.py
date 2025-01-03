"""Setup."""

from setuptools import setup

with open("README.md", encoding="utf8") as fid:
    long_description = fid.read()  # pylint: disable=invalid-name

TEST_DEPS = [
    "mock",
    "pytest",
]

EXTRAS = {
    "test": TEST_DEPS,
}

setup(
    author="NIWC Pacific",
    name="statick-web",
    description="Statick analysis plugins for Web (css, html, js) files.",
    version="0.2.0",
    packages=[
        "statick_tool",
        "statick_tool.plugins.discovery",
        "statick_tool.plugins.tool",
    ],
    package_dir={
        "statick_tool": ".",
        "statick_tool.plugins.discovery": "src/statick_web/plugins/discovery",
        "statick_tool.plugins.tool": "src/statick_web/plugins/tool",
    },
    package_data={
        "statick_tool": ["rsc/.*", "rsc/*"],
        "statick_tool.plugins.discovery": ["*.yapsy-plugin"],
        "statick_tool.plugins.tool": ["*.yapsy-plugin"],
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["statick"],
    tests_require=TEST_DEPS,
    extras_require=EXTRAS,
    url="https://github.com/sscpac/statick-web",
    classifiers=[
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Testing",
    ],
)
