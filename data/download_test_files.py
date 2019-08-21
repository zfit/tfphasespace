import wget

files_urls = [
    ('B2K1Gamma_RapidSim_7TeV_K1KstarNonResonant_Tree.root',
     'https://cernbox.cern.ch/index.php/s/8mN10X8U7VGfaRc/download'),
    ('B2K1Gamma_RapidSim_7TeV_Tree.root', 'https://cernbox.cern.ch/index.php/s/pr3aM8n2hPT4Pag/download'),
    ('B2KstGamma_RapidSim_7TeV_KstarNonResonant_Tree.root',
     'https://cernbox.cern.ch/index.php/s/QuP2cHeISTTSLVv/download'),
    ('B2KstGamma_RapidSim_7TeV_Tree.root', 'https://cernbox.cern.ch/index.php/s/EH5yrCpGko7P7Mc/download')]


def download(url, file_name):
    return wget.download(url=url, bar=False)


if __name__ == '__main__':
    files = [download(url=url, file_name=file) for file, url in files_urls]
