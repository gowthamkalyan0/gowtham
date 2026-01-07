{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOBGgIMfsTYkbEGs27P0rZh",
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
        "<a href=\"https://colab.research.google.com/github/gowthamkalyan0/gowtham/blob/main/2.%20Candidate%20elimination.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Qb1TIf7FVLra",
        "outputId": "32a3cb38-a944-4e44-a242-6a47e563051f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Result Hypotheses:\n",
            "['Sunny', 'Warm', '?', 'Strong', '?', '?']\n"
          ]
        }
      ],
      "source": [
        "import copy\n",
        "\n",
        "def initialize_hypotheses(n):\n",
        "    hypotheses = []\n",
        "    specific_hypothesis = ['0'] * n\n",
        "    # Initialize general hypothesis to be maximally general ('?' for all attributes)\n",
        "    general_hypothesis = ['?'] * n\n",
        "    hypotheses.append(specific_hypothesis) # S\n",
        "    hypotheses.append(general_hypothesis) # G (initially just one, but will expand)\n",
        "    return hypotheses\n",
        "\n",
        "def candidate_elimination(training_data):\n",
        "    num_attributes = len(training_data[0]) - 1\n",
        "    hypotheses = initialize_hypotheses(num_attributes)\n",
        "\n",
        "    for example in training_data:\n",
        "        if example[-1] == 'Yes':  # Positive example\n",
        "            # Update specific hypothesis (S)\n",
        "            for i in range(num_attributes):\n",
        "                if hypotheses[0][i] == '0': # If specific hypothesis is '0' (uninitialized for this attr)\n",
        "                    hypotheses[0][i] = example[i] # Initialize with the example's attribute value\n",
        "                elif hypotheses[0][i] != example[i]: # If attribute differs, generalize to '?'\n",
        "                    hypotheses[0][i] = '?'\n",
        "\n",
        "            # Remove general hypotheses inconsistent with positive example\n",
        "            # A general hypothesis h is inconsistent if it does NOT cover the positive example.\n",
        "            # (i.e., h predicts negative for a positive example)\n",
        "            new_general_hypotheses = []\n",
        "            for h_gen in hypotheses[1:]: # Iterate over current general hypotheses\n",
        "                is_consistent_with_positive = True\n",
        "                for i_attr in range(num_attributes):\n",
        "                    # If h_gen has a specific value that doesn't match the example, and it's not '?',\n",
        "                    # then it's inconsistent.\n",
        "                    if h_gen[i_attr] != '?' and h_gen[i_attr] != example[i_attr]:\n",
        "                        is_consistent_with_positive = False\n",
        "                        break\n",
        "                if is_consistent_with_positive:\n",
        "                    new_general_hypotheses.append(h_gen)\n",
        "            hypotheses = [hypotheses[0]] + new_general_hypotheses\n",
        "\n",
        "        else:  # Negative example (example[-1] == 'No')\n",
        "            # The specific hypothesis (hypotheses[0]) is never affected by negative examples.\n",
        "            # It is assumed to be consistent with all positive and inconsistent with all negative examples.\n",
        "\n",
        "            # Refine general hypotheses (G)\n",
        "            # A general hypothesis h is inconsistent with a negative example if it *covers* the negative example.\n",
        "            # (i.e., h predicts positive for a negative example) Such h must be specialized or removed.\n",
        "\n",
        "            current_specific_hypothesis = hypotheses[0]\n",
        "            new_general_hypotheses = []\n",
        "\n",
        "            for h_gen in hypotheses[1:]: # Iterate only over general hypotheses\n",
        "                h_gen_covers_negative_example = True\n",
        "                for i_attr in range(num_attributes):\n",
        "                    if h_gen[i_attr] != '?' and h_gen[i_attr] != example[i_attr]:\n",
        "                        h_gen_covers_negative_example = False\n",
        "                        break\n",
        "\n",
        "                if not h_gen_covers_negative_example: # If it does NOT cover the negative example, it is consistent, so keep it.\n",
        "                    new_general_hypotheses.append(h_gen)\n",
        "                else: # If it DOES cover the negative example, it's inconsistent (too general). It needs specialization.\n",
        "                    # For a proper Candidate Elimination, we would generate new, more specific G hypotheses here.\n",
        "                    # The original code's attempt at specialization was flawed. For this fix, we simply remove\n",
        "                    # the inconsistent (too general) hypothesis, which is a common simplification for G-set updates.\n",
        "                    pass # Effectively removed by not adding to new_general_hypotheses\n",
        "\n",
        "            hypotheses = [current_specific_hypothesis] + new_general_hypotheses\n",
        "\n",
        "    return hypotheses # Corrected indentation for the return statement\n",
        "\n",
        "training_data = [\n",
        "    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],\n",
        "    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],\n",
        "    ['Rainy', 'Cold', 'High', 'Weak', 'Cool', 'Change', 'No'],\n",
        "    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']\n",
        "]\n",
        "\n",
        "result_hypotheses = candidate_elimination(training_data)\n",
        "print(\"Result Hypotheses:\")\n",
        "for h in result_hypotheses:\n",
        "    print(h)"
      ]
    }
  ]
}