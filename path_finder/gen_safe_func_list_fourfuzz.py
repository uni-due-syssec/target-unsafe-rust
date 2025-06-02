import os
import sys
import subprocess
import networkx
    
def generate_cgs(cg_dir):
    build_files = os.listdir(cg_dir)
    
    for f in build_files:
        if f.endswith(".bc"):
            f_path = os.path.join(cg_dir, f)
            opt = os.path.join(os.environ["RUST_HOME"], "lib", "rustlib", "x86_64-unknown-linux-gnu", "bin", "opt")
            command = [opt, "-callgraph-dot-filename-prefix="+f, "-passes=dot-callgraph", "-disable-output", f_path]
            subprocess.run(command, cwd = cg_dir, check = True)
    
    counter = 0
    build_files = os.listdir(cg_dir)
    
    for f in build_files:
        if f.endswith("callgraph.dot"):
            counter +=1
    return counter

def fix_graph(graph_dir):
    build_files = os.listdir(graph_dir)
    for f in build_files:
        if f.endswith("callgraph.dot"):
            in_path = os.path.join(graph_dir, f)
            out_path = os.path.join(graph_dir, f.replace("callgraph.dot", "callgraph.fix.dot"))
            lines_seen = set()
            
            with open(out_path, "w") as out, open(in_path, "r") as in_f:
                for line in in_f.readlines():
                    if line not in lines_seen:
                        out.write(line)
                        lines_seen.add(line)

def dedup_graph(G_cg):
    try:
        G_cg.remove_node("\\n")
    except networkx.exception.NetworkXError:
        pass
        
    unique_nodes = {}
    node_labels = networkx.get_node_attributes(G_cg, "label")
    
    for n in node_labels:
        label = node_labels[n]
        if label in unique_nodes:
            unique_nodes[label].append(n)
        else:
            unique_nodes[label] = [n]
    
    for n in unique_nodes:
        if len(unique_nodes[n])>1:
            for i in range(1, len(unique_nodes[n])):
                networkx.contracted_nodes(G_cg, unique_nodes[n][0], unique_nodes[n][i], copy = False)

def merge_cg_graphs(cg_dir):
    build_files = os.listdir(cg_dir)
    G_cg = networkx.DiGraph()
    for f in build_files:
        if f.endswith("callgraph.fix.dot"):
            in_path = os.path.join(cg_dir, f)
            G_cg.update(networkx.DiGraph(networkx.drawing.nx_pydot.read_dot(in_path)))
            dedup_graph(G_cg)

    return G_cg


def generate_blacklist(G_cg, program_name, path_unsafe_func):
    node_labels = networkx.get_node_attributes(G_cg, "label")

    safe_f_path = os.path.join("denylist."+program_name+".txt")
    
    unsafe_functions_s = []
    
    with open(path_unsafe_func, "r") as fp:
        unsafe_functions_s = fp.read().splitlines()

    unsafe_hashes = []

    for uf in unsafe_functions_s:
        if uf and not uf.startswith("#"):
            temp =  uf[-17:-1]
            if temp not in unsafe_hashes:
                unsafe_hashes.append(temp)
    
    unsafe_functions = []
    
    for h in unsafe_hashes:
        for node in node_labels:
            if h in node_labels[node]:
                unsafe_functions.append(node)
    
    only_safe = []
    doublicates = 0

    for n in G_cg.nodes():
        if n not in unsafe_functions:
             is_unsafe = False
             for un in unsafe_functions:
                 if networkx.has_path(G_cg, n, un):
                     is_unsafe = True
                     break
             if not is_unsafe:
                if n not in only_safe:
                    only_safe.append(n)
                else:
                    doublicates += 1

    with open(safe_f_path, "w") as safe_fp:
        for sn in only_safe:
            norm_name = node_labels[sn].replace("\"", "").replace("{","").replace("}","")
            safe_fp.write("fun: "+norm_name+"\n")
    
    print("[i] List written to:", safe_f_path)

def main():

    if len(sys.argv) != 4:
        print("[!] Usage: python3 gen_safe_func_list_fourfuzz.py path_to_deps_dir program_name path_to_unsafe_function_list")
        sys.exit(1)
    
    deps_dir = sys.argv[1]
    program_name = sys.argv[2]
    path_unsafe_func = sys.argv[3]

    cg_count = generate_cgs(deps_dir)
    
    fix_graph(deps_dir)
    
    G_cg = merge_cg_graphs(deps_dir)
    dedup_graph(G_cg)
    
    generate_blacklist(G_cg, program_name, path_unsafe_func)
    
if __name__ == '__main__':
    main()
