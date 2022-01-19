pragma solidity >=0.7.0;

// @ Record of contact between two or more individuals.
contract Contact {

    // Represents a single User.
    struct User {
        address user_address;
        string user_name;
        string user_key;
        string user_cipher;
    }

    // Dynamic array of Users.
    User[] user_list;

    // Map of users keyed by their name.
    mapping(string => User) user_map;

    // Represents a single message sent by any contactee.
    struct Message {
        address contract_address;
        uint message_number;
        User message_sender;
        string message_content;
    }

    uint message_count= 0;

    // Dynamically sized array of "Message" structs.
    Message[] message_archive;

    // Adds a new User to the contract.
    function addUser(string calldata newContacteeName, string calldata newContacteeKey) external returns (User[] memory) {
        user_list.push(User({user_address: msg.sender, user_name: newContacteeName, user_key: newContacteeKey}));
        return user_list;
    }
    
    // Validates a new user by storing the encrypted private key for them.
    function validateUser(string calldata newContacteeName, string calldata newContacteeCipher) external returns (user[] memory) {
    	user_map[newContacteeName].user_cipher = newContacteeCipher
    }

    function addMessage(string memory new_message_sender_name, string calldata new_message_content) external returns (Message[] memory) {
        message_count += 1;
        Message memory new_message = Message({contract_address: address(this), message_number: message_count, message_sender: User({user_address: msg.sender, user_name: new_message_sender_name}), message_content: new_message_content});
        message_archive.push(new_message);
        return getMessageArchive();
    }

    // Message archive getter.
    function getMessageArchive() private view returns (Message[] memory) {
        return message_archive;
    }

    // User list getter.
    function getUserList() private view returns (User[] memory) {
        return user_list;
    }
}
