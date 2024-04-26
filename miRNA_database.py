import sys
import pandas as pd
import argparse

print("""
####################
# LOADING DATABASE #
####################

###################
# DATABASE LOADED #
###################
""")

parser = argparse.ArgumentParser(description="Local database search tool for miRNAs and diseases")
parser.add_argument("-s", "--search", type=str, help="Look-up all miRNAs or diseases that contain a specified word i.e 'hsa' or 'dystrophy'. Disease names > 1 word must be in quotations.")
parser.add_argument("-m", "--miRNA", type=str, help="Look-up gene/disease information of a specified miRNA.")
parser.add_argument("-d", "--disease", type=str, help="Look-up miRNA/gene information of a specified disease. Disease name > 1 word must be in quotations.")
parser.add_argument("-smi", "--score_mi", type=float, nargs="?", const=80, help="Filter miRNA to Gene associations with confidence score.")
parser.add_argument("-sdis", "--score_dis", type=float, nargs="?", const=80, help="Filter Gene to Disease associations with confidence score.")


args = parser.parse_args()

# Import CSV and produce error if file is not found
try:
    cleaned_dataset_df = pd.read_csv("cleaned_dataset.csv")
except FileNotFoundError:
    print("ERROR: cleaned_dataset.csv file not found.")
    sys.exit()

# miRNA or disease look up ###################################################################
if args.search:
    # miRNA ---
    miRNA_search_result = cleaned_dataset_df["miRNA"].str.contains(args.search, case=False, na=False)
    unique_miRNA_values = cleaned_dataset_df["miRNA"][miRNA_search_result].unique()
    unique_miRNA_df = pd.DataFrame({"miRNA": unique_miRNA_values})
    # Disease ---
    disease_search_result = cleaned_dataset_df["Disease_name"].str.contains(args.search, case=False, na=False)
    unique_disease_values = cleaned_dataset_df["Disease_name"][disease_search_result].unique()
    unique_disease_df = pd.DataFrame({"Disease": unique_disease_values})

    # miRNA table
    if not unique_miRNA_df.empty:
        print("### Queried term:", args.search, "\n")
        print(unique_miRNA_df.to_markdown(index=False))

    # Disease_name table
    if not unique_disease_df.empty:
        print("### Queried term:", args.search, "\n")
        print(unique_disease_df.to_markdown(index=False))

    # Exit if both tables are empty
    if unique_miRNA_df.empty and unique_disease_df.empty:
        print("ERROR: Not found in database")
        sys.exit()


# miRNA search formatting (all combinations) #################################################
if args.miRNA:
    # Check for matches of args.miRNA
    filtered_miRNA = cleaned_dataset_df[cleaned_dataset_df["miRNA"] == args.miRNA]
    # Error if miRNA not found as is its not found length will = 0
    if len(filtered_miRNA) < 1:
        print("ERROR: miRNA not found in database")
        sys.exit()

    # Filter for miRNA confidence score if given
    if args.score_mi:
        filtered_miRNA = filtered_miRNA[filtered_miRNA["Score_mi"] >= args.score_mi]

    # Filter for disease confidence score if given
    if args.score_dis:
        filtered_miRNA = filtered_miRNA[filtered_miRNA["Score_dis"] >= args.score_dis]

    # Display necessary columns
    if args.score_mi and args.score_dis:
        print(" ### Queried miRNA:", args.miRNA, "\n", "### Filtered miRNA score:", args.score_mi, "\n", "### Filtered disease score:", args.score_dis, "\n")
        print(filtered_miRNA[["Score_mi", "Gene", "Disease_name", "Score_dis"]].to_markdown(index=False))
    elif args.score_mi:
        print(" ### Queried miRNA:", args.miRNA, "\n","### Filtered miRNA score:", args.score_mi, "\n")
        print(filtered_miRNA[["Score_mi", "Gene", "Disease_name"]].to_markdown(index=False))
    elif args.score_dis:
        print(" ### Queried miRNA:", args.miRNA, "\n", "### Filtered disease score:", args.score_dis, "\n")
        print(filtered_miRNA[["Gene", "Disease_name", "Score_dis"]].to_markdown(index=False))
    else:
        print("### Queried miRNA:", args.miRNA, "\n")
        print(filtered_miRNA[["Gene", "Disease_name"]].to_markdown(index=False))


# Disease search formatting (all combinations) ##################################################
if args.disease:
    # Check for matches of args.disease
    filtered_disease = cleaned_dataset_df[cleaned_dataset_df["Disease_name"] == args.disease]
    # Error if disease name not found as if its not found length will = 0
    if len(filtered_disease) < 1:
        print("ERROR: Disease not found in database")
        sys.exit()

    # Filter disease confidence score if given
    if args.score_dis:
        filtered_disease = filtered_disease[filtered_disease["Score_dis"] >= args.score_dis]

    # Filter miRNA confidence score if given
    if args.score_mi:
        filtered_disease = filtered_disease[filtered_disease["Score_mi"] >= args.score_mi]

    # Display necessary columns
    if args.score_dis and args.score_mi:
        print(" ### Queried disease:", args.disease, "\n", "### Filtered miRNA score:", args.score_mi, "\n", "### Filtered disease score:", args.score_dis, "\n")
        print(filtered_disease[["miRNA", "Score_mi", "Gene", "Score_dis"]].to_markdown(index=False))
    elif args.score_dis:
        print(" ### Queried disease:", args.disease, "\n", "### Filtered disease score:", args.score_dis, "\n")
        print(filtered_disease[["miRNA", "Gene", "Score_dis"]].to_markdown(index=False))
    elif args.score_mi:
        print(" ### Queried disease:", args.disease, "\n", "### Filtered miRNA score:", args.score_mi, "\n")
        print(filtered_disease[["miRNA", "Score_mi", "Gene"]].to_markdown(index=False))
    else:
        print(" ### Queried disease:", args.disease, "\n")
        print(filtered_disease[["miRNA", "Gene"]].to_markdown(index=False))
