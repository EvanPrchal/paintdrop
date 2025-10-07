type ButtonProps = {
  backgroundColor: string;
  borderColor: string;
  textColor: string;
  text: string;
};

const Button: React.FC<ButtonProps> = ({ backgroundColor, borderColor, textColor, text }) => {
  return (
    <div>
      <button
        className={`rounded-full px-4 w-3xs border-4 text-body border-paint-grey text-paint-grey 
             ${backgroundColor} hover:bg-paint-grey active:bg-paint-black ${borderColor} ${textColor}`}
      >
        {text}
      </button>
    </div>
  );
};

export default Button;
