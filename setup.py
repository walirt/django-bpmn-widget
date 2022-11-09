from setuptools import setup

setup(
    name="django-bpmn-widget",
    version="0.0.1",
    description="django bpmn modeler widget(integrated with properties panel)",
    url="https://github.com/walirt/django-bpmn-widget",
    author="walirt",
    author_email="610577219@qq.com",
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="django, bpmn, widget",
    packages=["bpmn_widget"],
    include_package_data=True,
    python_requires=">=3",
    install_requires=["Django"],
    project_urls={
        "Source": "https://github.com/walirt/django-bpmn-widget",
        "Bug Reports": "https://github.com/walirt/django-bpmn-widget/issues"
    }
)
