# -*- coding: utf-8 -*-
import sys
from DataAccess import DownloadData


def main(Dir, Startdate='', Enddate='',
         latlim=[-50, 50], lonlim=[-180, 180], cores=False):
                """
                This function downloads daily CHIRPS data

                Keyword arguments:
                Dir -- 'C:/file/to/path/'
                Startdate -- 'yyyy-mm-dd'
                Enddate -- 'yyyy-mm-dd'
                latlim -- [ymin, ymax] (values must be between -50 and 50)
                lonlim -- [xmin, xmax] (values must be between -180 and 180)
                cores -- The number of cores used to run the routine.
                         It can be 'False' to avoid using parallel computing
                         routines.
                """
                # Download data
                DownloadData(Dir, Startdate, Enddate, latlim, lonlim, cores,
                             TimeCase='daily')

if __name__ == '__main__':
    main(sys.argv)
