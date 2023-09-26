import av
import av.datasets


content = av.datasets.curated('C:\\Users\\Ian\\Downloads\\xinwenlianbo-20230815 19_00 2023-08-16 14_05.mp4')
with av.open(content) as container:
    # Signal that we only want to look at keyframes.
    stream = container.streams.video[0]
    stream.codec_context.skip_frame = "NONKEY"

    counter = 0
    for frame in container.decode(stream):
        counter += 1
        print(f"保存第 {counter} 张图片")
        # We use `frame.pts` as `frame.index` won't make must sense with the `skip_frame`.
        frame.to_image().save(
            f"keyframe\\night-sky.{frame.pts}.jpg",
            quality=80,
        )
