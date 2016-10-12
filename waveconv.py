from astropy.io import fits

dir=''
inputfiles=['/home/aferreira/Dropbox/Doutorado/Dados/Spectra/conv/iraf_HARPS.GBOG_betGem_860']
n=len(inputfiles)
dirout=''

for i in inputfiles:
    spec=fits.open(dir+i+'.fits')

    prihdr = fits.Header()
    prihdr["NAXIS1"] = spec[0].data.size
    prihdr["CDELT1"] = spec[0].header['CDELT1']*10
    prihdr["CRVAL1"] = spec[0].header['CRVAL1']*10

    fits.writeto(dirout+i+'_wv.fits', spec[0].data, prihdr, clobber=True)
    spec.close()    

