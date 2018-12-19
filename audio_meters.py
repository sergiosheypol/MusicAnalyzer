import subprocess


class AudioMeters:

    @staticmethod
    def get_loudness(file_location):
        command = ['ffmpeg', '-nostats', '-i', file_location, '-filter_complex', 'ebur128=peak=true', '-f', 'null', '-']
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, universal_newlines=True)
        summary = output.split("Summary:")[-1]
        integrated_loudness = summary.split("Integrated loudness:", 1)[1].split("Loudness range:", 1)[0]
        integrated_loudness_i = integrated_loudness.split("I:", 1)[1].split("Threshold:", 1)[0].split("LUFS", 1)[
            0].strip()
        true_peak = summary.split("True peak:", 1)[1].strip()
        true_peak_peak = true_peak.split("Peak:", 1)[1].split("dBFS", 1)[0].strip()
        stats = {}
        stats['Integrated Loudness'] = {}
        stats['Integrated Loudness']['I'] = float(integrated_loudness_i)
        stats['True Peak'] = {}
        stats['True Peak']['Peak'] = float(true_peak_peak)
        return stats
