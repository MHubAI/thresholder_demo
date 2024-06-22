import SimpleITK as sitk
import argparse
    
def main():
    # argparse cli setup
    parser = argparse.ArgumentParser(description='Threshold an image')
    parser.add_argument('-i', '--input', help='The input image')
    parser.add_argument('-o', '--output', help='The output image')
    parser.add_argument('-l', '--lower', type=float, help='The lower threshold')
    parser.add_argument('-u', '--upper', type=float, help='The upper threshold')
    args = parser.parse_args()
    
    # load input image
    input_image = sitk.ReadImage(args.input)
    
    # threshold image
    thresholded_image = sitk.BinaryThreshold(input_image, args.lower, args.upper, 1, 0)
    
    # save output image
    sitk.WriteImage(thresholded_image, args.output)
    
if __name__ == '__main__':
  main()
  
  