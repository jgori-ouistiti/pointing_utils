from pointing_utils.throughput import FittsModel
import pathlib

original_dataset_directory = pathlib.Path(__file__).resolve().parents[0]


def test_without_CI():
    fm = FittsModel((original_dataset_directory / "fitts.csv").resolve())
    return fm


def test_with_CI_bootstrap():
    fm = FittsModel(
        (original_dataset_directory / "fitts.csv").resolve(),
        CI="bootstrap",
        bootstrap_kwargs={"batch": 100, "n_resamples": 9999},
    )
    return fm


def test_with_CI_delta():
    fm = FittsModel(
        (original_dataset_directory / "fitts.csv").resolve(),
        CI="delta",
    )
    return fm


if __name__ == "__main__":
    fm_wo_ci = test_without_CI()
    fm_w_d = test_with_CI_delta()
    fm_w_b = test_with_CI_bootstrap()
    import matplotlib.pyplot as plt

    fig, axs = plt.subplots(nrows=2, ncols=3)

    fm_w_b.plot_fitts_ID_all(axs[0, 0], reg=True)
    fm_w_b.plot_fitts_IDe_all(axs[0, 1], reg=True)
    fm_w_b.plot_fitts_IDepsilon_all(axs[0, 2], reg=True)
    fm_w_b.plot_fitts_ID_agg(axs[1, 0], reg=True)
    fm_w_b.plot_fitts_IDe_agg(axs[1, 1], reg=True)
    fm_w_b.plot_fitts_IDepsilon_agg(axs[1, 2], reg=True)

    plt.show()
