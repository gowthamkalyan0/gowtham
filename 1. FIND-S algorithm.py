{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO3Lzgu359brfshRPzgf6pd",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/gowthamkalyan0/gowtham/blob/main/1.%20FIND-S%20algorithm.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Qb1TIf7FVLra",
        "outputId": "3e2e98fe-dca7-4bec-fdc0-3fe64de2406f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Result Hypothesis: ['Sunny', 'Warm', '?', 'Strong', '?', '?']\n"
          ]
        }
      ],
      "source": [
        "def find_s_algorithm(training_data):\n",
        "    hypothesis = training_data[0][:-1]\n",
        "    for instance in training_data:\n",
        "        example_features = instance[:-1]\n",
        "        label = instance[-1]\n",
        "        if label == 'Yes':\n",
        "            for i in range(len(hypothesis)):\n",
        "                if example_features[i] != hypothesis[i]:\n",
        "                    hypothesis[i] = '?'\n",
        "    return hypothesis\n",
        "training_data = [\n",
        "    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],\n",
        "    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],\n",
        "    ['Rainy', 'Cold', 'High', 'Weak', 'Cool', 'Change', 'No'],\n",
        "    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']\n",
        "]\n",
        "result_hypothesis = find_s_algorithm(training_data)\n",
        "print(\"Result Hypothesis:\", result_hypothesis)"
      ]
    }
  ]
}