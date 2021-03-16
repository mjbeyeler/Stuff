function [RGB] = get_rgb_smooth(image,vessel_positions,layers)
% this function returns the median pixelwalue of the square of size
% -layer:layer around each position

[m, n] = ndgrid(-layers:layers, -layers:layers);

vessel_positions_x = repmat(vessel_positions(:,1),1,numel(m))...
    + repmat(m(:)',size(vessel_positions,1),1);
vessel_positions_y = repmat(vessel_positions(:,2),1,numel(m))...
    + repmat(n(:)',size(vessel_positions,1),1);

RGB = [median(image(sub2ind(size(image),vessel_positions_x,vessel_positions_y,ones(length(vessel_positions),numel(m))*1)),2)...
    median(image(sub2ind(size(image),vessel_positions_x,vessel_positions_y,ones(length(vessel_positions),numel(m))*2)),2)...
    median(image(sub2ind(size(image),vessel_positions_x,vessel_positions_y,ones(length(vessel_positions),numel(m))*3)),2)];

end