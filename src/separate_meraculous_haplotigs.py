#!/usr/bin/env python3

from Bio import SeqIO
import copy
import os
import re
import tompytools

# output
outdir = 'output/meraculous_haplotigs'
if not os.path.isdir(outdir):
    os.mkdir(outdir)

# files
haplotigs_fasta = ('data/meraculous_diploid2/meraculous_merblast/'
                   'haplotigs.filtered.fa')
isotig_file = os.path.join(outdir, 'dd_isotigs.fa')
h1_file = os.path.join(outdir, 'haplotigs_p1.fa')
h2_file = os.path.join(outdir, 'haplotigs_p2.fa')

# read the fasta file
tompytools.generate_message('Reading haplotigs from file\n%s' % haplotigs_fasta)
records = list(SeqIO.parse(haplotigs_fasta, 'fasta'))

# separate haplotigs and diplotigs
tompytools.generate_message('Extracting isotigs')
isotigs = [x for x in records if 'isotigDD' in x.name]
tompytools.generate_message('Extracting and renaming p1 diplotigs')
haplotig_1 = [remove_haplotig_suffix(x) for x in records if '_p1' in x.name]
tompytools.generate_message('Extracting and renaming p2 diplotigs')
haplotig_2 = [remove_haplotig_suffix(x) for x in records if '_p2' in x.name]

# write output to disk
tompytools.generate_message('Writing isotigs to file\n%s' % isotig_file)
SeqIO.write(
    sequences=isotigs,
    handle=isotig_file,
    format='fasta')

tompytools.generate_message('Writing p1 diplotigs to file\n%s' % h1_file)
SeqIO.write(
    sequences=haplotig_1,
    handle=h1_file,
    format='fasta')

tompytools.generate_message('Writing p2 diplotigs to file\n%s' % h2_file)
SeqIO.write(
    sequences=haplotig_2,
    handle=h2_file,
    format='fasta')