from calendar import c
import sys, time
# TODO: uncomment
# import TimeTagger


def main():
    # get run time and coincident window args
    run_time = sys.argv[1]
    coin_time = sys.argv[2]
    
    # make default counts list if try fails
    counts = [100,150,30]

    # # time tagger (tt) serial number
    # tagger_serial = '1948000SAR'
    # # run time in sec
    # run_time = 10
    # # coincidence window in ps
    # coincidence_window = 3
    # # tt hardware channels
    # hardware_channels = [1,2]

    # # connect to the tt and reset it
    # tagger = TimeTagger.createTimetagger(tagger_serial)
    # tagger.reset()

    # # wrap in try so if something goes wrong it doesn't mess up
    # #   the tt for the next attempt
    # try:
    #     # set up a virtual coincidence channel between the hardware channels
    #     coincidence_window_ps = coincidence_window * 1000
    #     run_time_ps = run_time * int(1e12)
    #     coincidence_channel = TimeTagger.Coincidence(tagger, hardware_channels,
    #                                                  coincidence_window_ps)
    #     # start a countrate measurement using the harware and virtual channels
    #     channels = [1,2,coincidence_channel.getChannel()]
    #     measurement = TimeTagger.Countrate(tagger, channels)
    
    #     # when taking a measurement it does not start immediately
    #     # sync-ing is nessisary for the tt to configure its fpga, ...
    #     tagger.sync()
    
    #     measurement.startFor(run_time_ps)
    #     measurement.waitUntilFinished()
    
    #     # stop measurement and record the data
    #     measurement.stop()
    #     count_rates = measurement.getData()
    #     counts = measurement.getCountsTotal()
    
    # # do even if the try fails
    # finally:
    #     TimeTagger.freeTimeTagger(tagger)
    
    # a_counts, b_counts, coins
    for count in counts:
        print(count)

if __name__ == '__main__':
    main()