
import conllu


# Path to your CoNLL-U file
file_path = './en_ewt-ud-train.conllu'




'''
i = 0
# Iterate through each sentence
for sentence in sentences:
    # Iterate through each token in the sentence
    if i >25:
            break
    for token in sentence:
        i+=1
        # Print or process each token (row)
        print(token)
        # Accessing specific fields
        print(f"ID: {token['id']}, Form: {token['formm']}, POS: {token['upostag']}, Lemma: {token['lemma']}")
'''



def create_filtered_conllu(input_path, output_path, columns):
    with open(input_path, 'r', encoding='utf-8') as file:#utf-8 as the data corpus
        # Parse the content of the file
        sentences = conllu.parse(file.read())

    i=0
    with open(output_path, 'w', encoding='ascii') as out_file:#Ascii output to work with the crfsuite library
        for sentence in sentences:
            for token in sentence:
                i+=1
                #if i > 10000:
                 #   break
                # Write only the selected columns
                try:
                    #edit the below depending on ur needs
                    out_file.write(f"{token[columns[0]]}\t{token[columns[1]]}\t{token[columns[2]]}\n")
                    #out_file.write(f"{token[columns[0]]}\t{token[columns[1]]}\t0\n")
                    #out_file.write(f"{token[columns[0]]}\t0\t0\n")
                except Exception as e:
                    print("Error:", e, "\t" , i)
            # Add a blank line to separate sentences
            out_file.write("\n")
            i+=1






# Path to the new filtered CoNLL-U file
output_path = './train_pos_hmm.conllu'

# Columns to keep in the new file
columns_to_keep = [ 'form', 'upostag' , 'xpostag']

# Create the filtered CoNLL-U file
#create_filtered_conllu(file_path, output_path, columns_to_keep)
file_path2 = "./en_ewt-ud-test.conllu"
output_path2 = "./test_pos_hmm.conllu"

file_path3 = "./en_ewt-ud-test2.conllu"
output_path3 = "./test_pos.conllu"

output_path4 = "./test_pos2_hmm.conllu"



create_filtered_conllu(file_path2, output_path3, columns_to_keep)
        


