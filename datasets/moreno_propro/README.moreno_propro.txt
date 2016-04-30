Protein network, part of the Koblenz Network Collection
===========================================================================

This directory contains the TSV and related files of the moreno_propro network:

This undirected network contains protein interactions contained in yeast. Research showed that proteins with a high degree were more important for the surivial of the yeast than others. A node represents a protein and an edge represents a metabolic interaction between two proteins.  The network contains loops.


More information about the network is provided here: 
http://konect.uni-koblenz.de/networks/moreno_propro

Files: 
    meta.moreno_propro -- Metadata about the network 
    out.moreno_propro -- The adjacency matrix of the network in space separated values format, with one edge per line
      The meaning of the columns in out.moreno_propro are: 
        First column: ID of from node 
        Second column: ID of to node


Complete documentation about the file format can be found in the KONECT
handbook, in the section File Formats, available at:

http://konect.uni-koblenz.de/publications

All files are licensed under a Creative Commons Attribution-ShareAlike 2.0 Germany License.
For more information concerning license visit http://konect.uni-koblenz.de/license.



Use the following References for citation:

@MISC{konect:2016:moreno_propro,
    title = {Protein network dataset -- {KONECT}},
    month = jan,
    year = {2016},
    url = {http://konect.uni-koblenz.de/networks/moreno_propro}
}

@article{konect:coulomb2005,
  title={Gene Essentiality and the Topology of Protein Interaction Networks},
  author={Coulomb, St{\'e}phane and Bauer, Michel and Bernard, Denis and Marsolier-Kergoat, Marie-Claude},
  journal={Proceedings of the Royal Society B: Biological Sciences},
  volume={272},
  number={1573},
  pages={1721--1725},
  year={2005},
  publisher={The Royal Society}
}

@article{konect:han2005,
  title={Effect of Sampling on Topology Predictions of Protein-Protein Interaction Networks},
  author={Han, Jing-Dong J and Dupuy, Denis and Bertin, Nicolas and Cusick, Michael E and Vidal, Marc},
  journal={Nature Biotechnology},
  volume={23},
  number={7},
  pages={839--844},
  year={2005},
  publisher={Nature Publishing Group}
}

@article{konect:stumpf2005,
  title={Subnets of Scale-free Networks are not Scale-free: Sampling Properties of Networks},
  author={Stumpf, Michael PH and Wiuf, Carsten and May, Robert M},
  journal={Proceedings of the National Academy of Sciences of the United States of America},
  volume={102},
  number={12},
  pages={4221--4224},
  year={2005},
  publisher={National Academy of Sciences}
}


@inproceedings{konect,
	title = {{KONECT} -- {The} {Koblenz} {Network} {Collection}},
	author = {Jérôme Kunegis},
	year = {2013},
	booktitle = {Proc. Int. Conf. on World Wide Web Companion},
	pages = {1343--1350},
	url = {http://userpages.uni-koblenz.de/~kunegis/paper/kunegis-koblenz-network-collection.pdf}, 
	url_presentation = {http://userpages.uni-koblenz.de/~kunegis/paper/kunegis-koblenz-network-collection.presentation.pdf},
}


