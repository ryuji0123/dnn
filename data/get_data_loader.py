from torch.utils.data import DataLoader


def getDataLoader(batch_size, dataset, num_workers=2, sampler=None):
    return DataLoader(
            batch_size=batch_size,
            dataset=dataset,
            num_workers=num_workers,
            pin_memory=True,
            sampler=sampler,
            shuffle=False if sampler is not None else True
            )
