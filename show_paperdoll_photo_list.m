function show_paperdoll_photo_list
  paperdoll_file = 'paperdoll_dataset.mat';
  load(paperdoll_file, 'samples');
  download_photos(samples);
end

function download_photos(samples)
  for i = 1:length(samples)
      sample = samples(i);
      printf('%07d.jpg,%s\n', sample.id, sample.url);
  end
end
